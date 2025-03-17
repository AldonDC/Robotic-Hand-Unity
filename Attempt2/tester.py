from finger import Finger
import matplotlib.pyplot as plt
import numpy as np

fing = Finger()

fing.changeAngles([0,np.pi/4, np.pi/4])
new_angles = [0, np.pi/2 + 0.1, 0.1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

fing.plot_finger(ax, 'b')
Force = [0, 0, -1, 0, 0, 0]
fing.plotForce(Force, ax)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(0, 5)
ax.set_ylim(-2.5,5)
ax.set_zlim(0, 5)
ax.set_aspect('equal')
plt.show()