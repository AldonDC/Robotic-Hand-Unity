# 🖐️ Robotic Hand Unity - Python API Integration  

![Project Banner](path/to/banner-image.png)  

## 📌 Overview  
This repository contains a **robotic hand simulation** developed in Unity, controlled using a **Python API (FastAPI)** for real-time kinematics.  

### 🌟 **Key Features**  
✅ **Unity-based robotic hand simulation**  
✅ **Python API for real-time movement control**  
✅ **Forward & Inverse Kinematics using `roboticstoolbox`**  
✅ **Seamless communication between Python & Unity**  

---

---

## 🚀 **Installation & Setup**
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AldonDC/Robotic-Hand-Unity.git
cd Robotic-Hand-Unity
```

### 2️⃣ Unity Setup  
- Open **Unity Hub**.  
- Add the `Robotic-Hand-Unity` project.  
- Install dependencies if required.  

### 3️⃣ Run the Python API  
Requires Python & FastAPI installed.  
```bash
cd API
pip install -r requirements.txt
uvicorn RobotAPI:app --reload
```
**📡 API Endpoint Example:**  
```
http://127.0.0.1:8000/0?link2=1.0
```

---

## 🔧 **How It Works**
This project integrates a **Python-based API** with Unity, allowing real-time robotic hand control.

### 📡 **Data Flow**  
1. The **Python API** computes the required joint angles.  
2. The API **sends** the data to Unity.  
3. Unity **processes the angles** and animates the robotic hand accordingly.  

![Data Flow Diagram](path/to/diagram.png)  

---

## 📸 Simulation Screenshots  
_📌 Add images here_  

![Simulation Screenshot](path/to/simulation-image.png)  

---

## 🔥 **Problems Solved**
_📌 Add problem descriptions and solutions_  

- **Issue:** Delay in movement synchronization.  
  - ✅ **Solution:** Optimized API requests with non-blocking I/O.  
- **Issue:** Inverse kinematics instability.  
  - ✅ **Solution:** Tuned optimization method for better convergence.  

---

## 🎮 **API Usage Example**
```python
import requests

url = "http://localhost:8000/{finger}"
params = {"link2": 1.0}
response = requests.get(url, params=params)
print(response.json())  # Expected output: {'newAngle': <calculated_angle>}
```

---

## 🛠️ **Technologies Used**
- **Unity** 🎮 for 3D simulation  
- **Python (FastAPI)** ⚡ for API communication  
- **Robotics Toolbox (`roboticstoolbox`)** 🤖 for kinematics  
- **Uvicorn** 🚀 for running the API  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

🚀 **_Feel free to contribute and improve this repository!_**
