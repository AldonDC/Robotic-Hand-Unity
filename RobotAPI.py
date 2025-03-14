from fastapi import FastAPI
from finger import Finger
from robot import Robot
import numpy as np

LinkLengths = [1,1]
fingers = [Finger("finger1", LinkLengths), Finger("finger2", LinkLengths), Finger("finger3", LinkLengths)]
gripper = Robot(fingers)

app = FastAPI()

@app.get("/{finger}")
def read_root(finger: int, link2: float):
    currAngle = gripper.fingers[finger].q
    currAngle += 0.1 * np.pi
    return {"newAngle": currAngle}