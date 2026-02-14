# 🚗 AI-Powered Smart Parking System

An AI-based Smart Parking System that detects available and occupied parking slots using **YOLO Object Detection** and Deep Learning.

This system helps reduce traffic congestion and saves time by automatically identifying empty parking spaces from parking lot images.

---

## 📌 Project Overview

Finding parking in crowded areas is time-consuming and stressful.  
This project solves that problem using **Computer Vision and Deep Learning**.

### 🔹 The System:

- Detects each parking slot  
- Classifies slots as **Empty** or **Occupied**  
- Highlights empty slots in 🔵 Blue  
- Highlights occupied slots in 🔴 Red  
- Displays total, empty, and occupied slot count  

---

## 🧠 Technologies Used

- Python  
- Flask  
- OpenCV  
- YOLO (Ultralytics)  
- HTML  
- CSS  

---

## ⚙️ How It Works

1. User uploads a parking lot image  
2. YOLO model detects parking slots  
3. System classifies each slot  
4. Bounding boxes are drawn:
   - 🔵 Blue → Empty  
   - 🔴 Red → Occupied  
5. Results are displayed with slot statistics  

---

## 📂 Project Structure

smart-parking-system/
│
├── static/
│ ├── input.jpg
│ ├── output.jpg
│ └── parking-bg.jpg
│
├── templates/
│ ├── home.html
│ ├── upload.html
│ ├── result.html
│ └── index.html
│
├── app.py
├── best.pt
└── smart-parking-1.ipynb


---

## 🚀 Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YaparlaBhargavi/smart-parking-system.git
cd smart-parking-system

2️⃣ Install Dependencies
pip install flask opencv-python ultralytics numpy

3️⃣ Run Application
python app.py


Open browser and visit:

http://127.0.0.1:5000/

🎯 Applications

Shopping Malls

Airports

Offices

Smart Cities

Industrial Parking Management

📈 Future Enhancements

Live CCTV integration

Cloud deployment

Database storage

Mobile app integration

IoT sensor connectivity

👩‍💻 Author

Yaparla Bhargavi
B.Tech CSE (Data Science)
AI & Machine Learning Enthusiast
