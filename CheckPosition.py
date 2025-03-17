from Object import Obstacle
from robot import Robot
import matplotlib.pyplot as plt
from spatialmath.base import transl, trotx, troty, trotz
import numpy as np
import spatialmath as sm

robot = Robot()
obstacle = Obstacle(1, 0, 1.5, 1, 5, 1)

# Modify fingers to starting configuration
robot.modifyFinger(1, (0, np.pi/2, 0))
robot.modifyFinger(2, (0, -np.pi/2, 0))
robot.modifyFinger(3, (0, -np.pi/2, 0))

# Establish robot contact points relative to the obstacle
obstacle.add_contact_point(transl(0,0, -0.5))
obstacle.add_contact_point(transl(0, -2, 0.5))
obstacle.add_contact_point(transl(0, 2, 0.5))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

robot.plot_layer(ax)
obstacle.plot_obstacle_layer(ax)


plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Transform the obstacle
transform = sm.SE3(trotx(np.pi/4) @ transl(0,0,0))
obstacle.modifyFrame(transform)

# Transform end-effector position
old_pos = robot.finger1.forward_kinematics()
new_pos = old_pos @ transform

new_pos = robot.inverse_kinematics(new_pos, 1)
print(new_pos)

obstacle.plot_obstacle_layer(ax)

plt.show()