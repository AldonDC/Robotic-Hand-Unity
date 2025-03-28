import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np
from Object import Obstacle

# Finger will be a two joint robot with an end effector represented as a semicircle with radius n

class Finger:
    def __init__(self, name="Robot_Finger", base=(0,0,0)):
        self.name = name
        links = []
        link0 = rtb.RevoluteMDH(a=0, alpha = np.pi/2)
        link1 = rtb.RevoluteMDH(a=1)
        link2 = rtb.RevoluteMDH(a=1)
        self.robot = rtb.DHRobot([link0, link1, link2], name=name)
        self.base = base
        self.robot.q = [0] * 3
        self.robot.base = sm.SE3(base)
        
        print(self.robot)

    def adjustPosition(self, q):
        self.robot.q = q        

    def plot(self, q):
        self.robot.q = q + [0]
        self.robot.plot(self.robot.q, backend="pyplot", block=True)
    
    def forward_kinematics(self):
        return self.robot.fkine(self.robot.q)
    
    def inverse_kinematics(self, T):
        return self.robot.ikine_LM(T)
    
    def move_to_collision_point(self, collision_point):
        # The collision point is an SE3 object (position) you want the robot to reach
        target = sm.SE3(collision_point)  # Target position for the end-effector
        
        # Use inverse kinematics to compute joint angles that reach the target
        q_solution = self.robot.ikine_LM(target)
        
        # Check if the solution is valid and update the robot's configuration
        if q_solution.success:
            self.adjustPosition(q_solution.q)  # Apply the joint angles
            print("Successfully moved to collision point:", collision_point)
        else:
            print("No valid solution found for the collision point:", collision_point)