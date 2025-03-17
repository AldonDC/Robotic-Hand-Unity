import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

link0 = rtb.RevoluteMDH(a=0, alpha = np.pi/2)
link1 = rtb.RevoluteMDH(a=1, alpha=0)
link2 = rtb.RevoluteMDH(a=1, alpha=0)

robot = rtb.DHRobot([link0, link1, link2], name="robot")

robot.plot((np.pi/4, np.pi/4, 0), block = "True")