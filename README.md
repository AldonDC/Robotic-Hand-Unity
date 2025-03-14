# 🖐️ Robotic Hand Unity - Python API Integration  

<p align="center">
  <img src="https://github.com/user-attachments/assets/69170457-058a-40eb-96dd-02b21ee13c6b" width="50%">
</p>

## 📌 Overview  
This repository contains a **robotic hand simulation** developed in Unity, controlled using a **Python API (FastAPI)** for real-time kinematics.  

### 🌟 **Key Features**  
✅ **Unity-based robotic hand simulation**  
✅ **Python API for real-time movement control**  
✅ **Forward & Inverse Kinematics using `roboticstoolbox`**  
✅ **Seamless communication between Python & Unity**  
✅ **Error handling and optimized logging**  
✅ **Smooth real-time updates with non-blocking API requests**  
✅ **Supports expansion for additional robotic movements**  

---

## 🎯 **Challenge & Goal**  
This simulation was created to **test real-time robotic control using Unity and Python**. The goal is to develop a scalable solution that enables:  
- **Accurate finger articulation** based on inverse kinematics.  
- **Dynamic communication between a physics engine (Unity) and an external API (Python).**  
- **Real-time adjustments and flexibility in motion handling.**  

### 💡 **Future Improvements**  
🔹 **WebSocket support** for even faster data transmission.  
🔹 **Machine learning-based motion prediction** to enhance movement fluidity.  
🔹 **Integration with real robotic hardware** for testing beyond simulation.  

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

## 📸 **Media Gallery**
### 🎥 **Simulation Videos**
_Add video links or GIFs showcasing the robotic hand movements in Unity._  

📹 [Watch the Full Simulation](path/to/video.mp4)  
📹 [Inverse Kinematics Demonstration](path/to/ik-demo.mp4)  

### 🖼️ **Screenshots of the Simulation**
_Add images here to visually explain the project._  

<p align="center">
  <img src="path/to/simulation-image1.png" width="45%">
  <img src="path/to/simulation-image2.png" width="45%">
</p>

<p align="center">
  <img src="path/to/simulation-image3.png" width="45%">
  <img src="path/to/simulation-image4.png" width="45%">
</p>

---

## 🔥 **Problems Solved**
_📌 Key challenges and solutions implemented:_  

- **Issue:** Delay in movement synchronization.  
  - ✅ **Solution:** Optimized API requests with non-blocking I/O.  
- **Issue:** Inverse kinematics instability.  
  - ✅ **Solution:** Tuned optimization method for better convergence.  
- **Issue:** Handling multiple finger movements in parallel.  
  - ✅ **Solution:** Implemented thread-safe handling in FastAPI.  
- **Issue:** Sudden API disconnection causing Unity freezing.  
  - ✅ **Solution:** Added error handling and automatic API reconnection logic.  

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
- **HTTP Requests** 📡 for Unity-Python communication  
- **Multithreading for parallel movement handling**  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

🚀 **_Feel free to contribute and improve this repository!_**
