'''
    Class for controlling a finger part of the end effector
    Contains
        - 3 links for robot configuration
            - Link 1 is just a rotation to work in the XZ plane
            - Link 2 is of length 1
            - Link 3 is of length 1
        - Base is dependent of which finger you are talking about
'''
import roboticstoolbox as rtb
import numpy as np

class Finger:
    # Initializes the finger object
    def __init__(self, name="Finger", base = (0,0,0)):
        
        # Declare robot joints
        link1 = rtb.RevoluteDH(a = 0, alpha = np.pi/2)
        link2 = rtb.RevoluteDH(a = 1, alpha = 0)
        link3 = rtb.RevoluteDH(a = 1, alpha = 0)

        # Initialize Robot
        self.finger = rtb.DHRobot([link1, link2, link3], name=name, base=base)
        self.base = base
        # Give robot initial angles
        self.q = [0,0,0]
        self.finger.q = self.q
    # Adds a finger to a matplotlib plot
    def plot_finger(self, ax, color):
        point1 = self.base
        point2 = [point1[0] + np.cos(self.q[1]), point1[1], point1[2] + np.sin(self.q[2])]
        point3 = [point2[0] + np.cos(self.q[1] + self.q[2]), point2[1], point2[2] + np.sin(self.q[1] + self.q[2])] 

        points = np.array([point1, point2, point3])
        ax.plot(points[:, 0], points[:, 1], points[:, 2], c=color)
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=color)
        print("Finger added to plot")
    # Changes the robot's current Angles
    def changeAngles(self, q):
        '''
        Changes the angles of the finger, Takes a list of size 3. Angles in radians
        '''
        newQ = q

        self.q = newQ
        self.finger.q = self.q
    # Calculates the currentJacobian using the current angle
    def calculateCurrentJacobian(self):
        '''
            Calculate the current Jacobian at the current angles 
        '''
        self.jacob = self.finger.jacob0(self.q)
        return self.jacob
    # Calculates the change in theta depending on the new theta values
    def calculateThetaChange(self, next_ang):
        '''
            Calculates the joint velocities for the next step
        '''
        theta_prev = np.array(self.q)
        theta_next = np.array(next_ang)
        theta_dot = (theta_next - theta_prev)

        return theta_dot
    # Calculates change of position of the end-effector given new angle values
    def EndEffectorChangePos(self, next_ang):
        return self.calculateCurrentJacobian() @ self.calculateThetaChange(next_ang)
    # Get the current pose of the end effector
    def getPose(self):
        return self.finger.fkine(self.q)
    # Get the force of the current end effector. Force is a force vector for angular and other torques 6x1
    def getJointTorques(self, oppositeForce):
        return self.calculateCurrentJacobian().T @ oppositeForce
    # Plot the value of the force
    def plotForce(self, oppositeForce, ax):
        origin = self.getJointPlacements()[2]
        force = self.getForce(oppositeForce)
        print(origin)
        ax.quiver(origin[0], origin[1], origin[2], -oppositeForce[0], -oppositeForce[1], -oppositeForce[2], color='black')
    # Get the end effector position
    def getJointPlacements(self):
        point1 = self.base
        point2 = [point1[0] + np.cos(self.q[1]), point1[1], point1[2] + np.sin(self.q[2])]
        point3 = [point2[0] + np.cos(self.q[1] + self.q[2]), point2[1], point2[2] + np.sin(self.q[1] + self.q[2])] 

        points = np.array([point1, point2, point3])
        self.JointPlacement = points
        return points
    # Map Object motion to contact
    def mapObjectMotionToContact(self, H, next_ang):
        return H @ self.EndEffectorChangePos(next_ang)
    # mapContactForcesToBase
    def mapContactForcesToBase(self, H, oppositeForce):
        return H @ oppositeForce