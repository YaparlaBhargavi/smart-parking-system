🚗 AI-Powered Smart Parking System

An AI-based Smart Parking System that detects available and occupied parking slots using YOLO Object Detection and Deep Learning.

This system helps reduce traffic congestion and saves time by automatically identifying empty parking spaces from parking lot images.

📌 Project Overview

Finding parking in crowded areas is time-consuming and stressful.
This project solves that problem by using Computer Vision and Deep Learning.

The system:

Detects each parking slot

Classifies slots as Empty or Occupied

Highlights empty slots in Blue

Highlights occupied slots in Red

Displays total, empty, and occupied slot count

🧠 Technologies Used

Python

Flask

OpenCV

YOLO (Ultralytics)

HTML

CSS

⚙️ How It Works

User uploads a parking lot image.

YOLO model detects parking slots.

The system classifies each slot.

Bounding boxes are drawn:

🔵 Blue → Empty

🔴 Red → Occupied

Results are displayed on a web page with slot counts.

📂 Project Structure
smart-parking/
│
├── static/
│   ├── input.jpg
│   ├── output.jpg
│   └── parking-bg.jpg
│
├── templates/
│   ├── home.html
│   ├── upload.html
│   ├── result.html
│   └── index.html
│
├── app.py
├── best.pt
└── smart-parking-1.ipynb

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/YaparlaBhargavi/smart-parking-system.git
cd smart-parking-system

2️⃣ Install Requirements
pip install flask opencv-python ultralytics numpy

3️⃣ Run the Application
python app.py


Open browser and go to:

http://127.0.0.1:5000/

🎯 Applications

Shopping Malls

Airports

Offices

Smart Cities

Industrial Parking Management

💡 Key Features

✔ Real-time detection
✔ Automatic slot counting
✔ Web-based interface
✔ Deep Learning powered
✔ Easy deployment

📈 Future Improvements

Live CCTV integration

Mobile application support

Database storage for slot history

IoT sensor integration

Real-time cloud deployment

👩‍💻 Author

Yaparla Bhargavi
B.Tech CSE (Data Science)
AI & Machine Learning Enthusiast
