from Object import Obstacle
import matplotlib.pyplot as plt
from spatialmath.base import transl, trotx, troty, trotz
import spatialmath as sm
import numpy as np
from robot import Robot

obstacle = Obstacle(1, 0, 1.5, 1, 5, 1)
robot = Robot()
# Establish robot contact points relative to the obstacle
obstacle.add_contact_point(transl(0,0, -0.5))
obstacle.add_contact_point(transl(0, -2, 0.5))
obstacle.add_contact_point(transl(0, 2, 0.5))

# Modify fingers to starting configuration
robot.modifyFinger(1, (0, np.pi/2, 0))
robot.modifyFinger(2, (0, -np.pi/2, 0))
robot.modifyFinger(3, (0, -np.pi/2, 0))

# Create rotation matrix
rot_matrix = sm.SO3.Rx(np.pi/9)

# Plot the object before and after rotation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

obstacle.plot_obstacle_layer(ax)

obstacle.modifyFrame2(rot_matrix)

obstacle.plot_obstacle_layer(ax)

contact_point = [obstacle.contact_points[0][0][3], obstacle.contact_points[0][1][3], obstacle.contact_points[0][2][3]]
print(contact_point)
print(type(contact_point))
robot.finger1.move_to_collision_point(contact_point)

q = np.array([np.pi / 4, np.pi / 4, 0])
s = robot.finger1.robot.jacob0(q)
print(s)
plt.show()