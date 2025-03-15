import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np
import matplotlib.pyplot as plt

class Obstacle:
    def __init__(self, x, y, z, length, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.frame = sm.SE3(x, y, z)
        half_length = length / 2
        half_width = width / 2
        half_height = height / 2
        
        self.corners = np.array([
            [-half_length + x, -half_width + y, -half_height + z],
            [half_length + x, -half_width + y, -half_height+ z],
            [half_length + x, half_width + y, -half_height+ z],
            [-half_length + x, half_width + y, -half_height + z],
            [-half_length + x, -half_width + y, half_height + z],
            [half_length + x, -half_width + y, half_height + z],
            [half_length + x, half_width + y, half_height + z],
            [-half_length + x, half_width + y, half_height + z]
        ])

        self.contact_points = []

    # Add a contact point relative to the frame
    def add_contact_point(self, point):
        newContactPoint = self.frame * point
        self.contact_points.append(newContactPoint)
    
    def plot_obstacle(self):
        transformed_corners = self.corners

        # Plot the result
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Define the 12 edges of the rectangular prism (pairs of corners)
        edges = [
            [transformed_corners[0], transformed_corners[1]],
            [transformed_corners[1], transformed_corners[2]],
            [transformed_corners[2], transformed_corners[3]],
            [transformed_corners[3], transformed_corners[0]],
            [transformed_corners[4], transformed_corners[5]],
            [transformed_corners[5], transformed_corners[6]],
            [transformed_corners[6], transformed_corners[7]],
            [transformed_corners[7], transformed_corners[4]],
            [transformed_corners[0], transformed_corners[4]],
            [transformed_corners[1], transformed_corners[5]],
            [transformed_corners[2], transformed_corners[6]],
            [transformed_corners[3], transformed_corners[7]]
        ]

        # Plot the edges
        for edge in edges:
            x_vals, y_vals, z_vals = zip(*edge)
            ax.plot3D(x_vals, y_vals, z_vals, color="r")

        # Plot the coordinate frame
        self.frame.plot(frame="C", color="blue", ax=ax)

        # Labels
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        plt.show()

    def plot_obstacle_layer(self, ax):
        transformed_corners = self.corners
        # Define the 12 edges of the rectangular prism (pairs of corners)
        edges = [
            [transformed_corners[0], transformed_corners[1]],
            [transformed_corners[1], transformed_corners[2]],
            [transformed_corners[2], transformed_corners[3]],
            [transformed_corners[3], transformed_corners[0]],
            [transformed_corners[4], transformed_corners[5]],
            [transformed_corners[5], transformed_corners[6]],
            [transformed_corners[6], transformed_corners[7]],
            [transformed_corners[7], transformed_corners[4]],
            [transformed_corners[0], transformed_corners[4]],
            [transformed_corners[1], transformed_corners[5]],
            [transformed_corners[2], transformed_corners[6]],
            [transformed_corners[3], transformed_corners[7]]
        ]

        # Plot the edges
        for edge in edges:
            x_vals, y_vals, z_vals = zip(*edge)
            ax.plot3D(x_vals, y_vals, z_vals, color="r")

        # Plot the coordinate frame
        self.frame.plot(frame="C", color="blue", ax=ax)

        print(self.contact_points)
        for point in self.contact_points:
            position = point[:3, 3]
            ax.scatter(position[0], position[1], position[2], c='black', marker='o')
        
        # Labels
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")

    def modifyFrame(self, transMatrix):
        self.frame = sm.SE3(self.frame * transMatrix)

        transformed_corners = []
        for corner in self.corners:
            corner_se3 = sm.SE3(corner[0], corner[1], corner[2])
            
            if not isinstance(transMatrix, sm.SE3):
                transMatrix = sm.SE3(transMatrix)

            transformed_corner = transMatrix * corner_se3

            transformed_corners.append(transformed_corner.t)
        
        self.corners = np.array(transformed_corners)
    