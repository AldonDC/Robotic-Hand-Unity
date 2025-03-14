import roboticstoolbox as rtb
from finger import Finger

class Robot:
    
    def _init__(self, fingers):
        self.fingers = fingers
    
    def forward_kinematics(self, q, finger_idx):
        # Implement forward kinematics for the robot
        return self.fingers[finger_idx].forward_kinematics(q)
    
    def inverse_kinematics(self, T, finger_idx):
        # Implement inverse kinematics for the robot
        return self.fingers[finger_idx].inverse_kinematics(T)
