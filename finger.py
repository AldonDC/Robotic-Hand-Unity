import roboticstoolbox as rtb

class Finger:
    def __init__(self, name, finger_lengths):
        self.name = name
        links = []
        for i in finger_lengths:
            links.append(rtb.RevoluteDH(a=0))
        
        self.robot = rtb.DHRobot(links, name=name)
        self.robot.q = [0] * len(finger_lengths)
    
    def forward_kinematics(self, q):
        return self.robot.fkine(q)
    
    def inverse_kinematics(self, T):
        return self.robot.ikine(T)
    
