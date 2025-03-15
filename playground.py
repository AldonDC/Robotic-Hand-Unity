from Object import Obstacle
import roboticstoolbox as rtb
import numpy as np
from spatialmath.base import transl, trotx, troty, trotz
import spatialmath as sm
from finger import Finger
from robot import Robot
import matplotlib.pyplot as plt

robot = Robot()
obstacle = Obstacle(1, 0, 1.5, 1, 5, 1)

robot.modifyFinger(1, (0, np.pi/2))
