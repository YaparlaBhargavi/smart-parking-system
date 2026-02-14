from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
model = YOLO("best.pt")

UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]

    if file and file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], "input.jpg")
        file.save(filepath)

        # 🔥 Stable detection settings
        results = model(
            filepath,
            conf=0.5,  # Higher confidence = less false detection
            iou=0.4,  # Control overlapping boxes
        )

        img = cv2.imread(filepath)

        total = 0
        empty = 0
        occupied = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                total += 1

                # 🎨 Thin professional highlight lines
                if cls == 0:  # Empty slot
                    empty += 1
                    color = (255, 120, 0)  # Blue-orange clean tone
                else:  # Occupied
                    occupied += 1
                    color = (0, 0, 255)  # Red

                # Thin rectangle (2px only)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

        output_path = os.path.join(app.config["UPLOAD_FOLDER"], "output.jpg")
        cv2.imwrite(output_path, img)

        return render_template(
            "result.html", total=total, empty=empty, occupied=occupied
        )

    return "Upload JPG or PNG file only!"


if __name__ == "__main__":
    app.run(debug=True)
