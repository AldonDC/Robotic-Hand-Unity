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

        for point in self.contact_points:
            position = point[:3, 3]
            ax.scatter(position[0], position[1], position[2], c='black', marker='o')
        
        # Labels
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")

    def modifyFrame1(self, transMatrix):
        self.frame = sm.SE3(self.frame * transMatrix)

        transformed_corners = []
        for corner in self.corners:
            corner_se3 = sm.SE3(corner[0], corner[1], corner[2])
            
            if not isinstance(transMatrix, sm.SE3):
                transMatrix = sm.SE3(transMatrix)

            transformed_corner = transMatrix * corner_se3

            transformed_corners.append(transformed_corner.t)
        
        new_contacts = []
        for coll in self.contact_points:
            coll = transMatrix * coll
            new_contacts.append(coll)
        
        self.contact_points = new_contacts
        self.corners = np.array(transformed_corners)

    def modifyFrame(self, rotMatrix):
        # Assuming rotMatrix is a 3x3 rotation matrix (no translation)
        rotation = sm.SO3(rotMatrix)  # Create a rotation object from the matrix

        # Apply the rotation to each corner (separating position and rotation)
        transformed_corners = []
        for corner in self.corners:
            # Apply rotation to the corner position (corner is a 3D numpy array)
            rotated_position = rotation * corner
            transformed_corners.append(rotated_position)

        # Apply the rotation to the contact points (which are numpy arrays)
        new_contacts = []
        for coll in self.contact_points:
            # Ensure we use only the first 3 components of the contact point
            rotated_contact = rotation * coll[:3]  # Take the first 3 components for rotation
            new_contacts.append(rotated_contact)
        
        # Update corners and contact points
        self.contact_points = new_contacts
        self.corners = np.array(transformed_corners)

        # The frame should remain unchanged, so do not modify it here
        # This ensures that the obstacle's origin (frame) stays fixed
    
    def modifyFrame2(self, rotMatrix):
        # Assuming rotMatrix is a 3x3 rotation matrix (no translation)
        rotation = sm.SO3(rotMatrix)  # Create a rotation object from the matrix

        # Apply the rotation to each corner (separating position and rotation)
        transformed_corners = []
        for corner in self.corners:
            # Apply rotation to the corner position (corner is a 3D numpy array)
            rotated_position = rotation * corner
            transformed_corners.append(rotated_position)

        # Apply the rotation to the contact points but only vary the Z-coordinate
        new_contacts = []
        for coll in self.contact_points:
            # Apply rotation to only the Z-coordinate, keeping X and Y the same
            x, y, z = coll[:3]  # Extract x, y, and z components
            
            # Create the 3D point to apply rotation to, but only modify Z
            rotated_point = rotation * np.array([x, y, z])  # Apply rotation to the full point
            new_contact = np.array([x, y, rotated_point[2]])  # Keep x, y fixed, update z
            
            new_contacts.append(new_contact)
        
        # Update corners and contact points
        self.contact_points = new_contacts
        self.corners = np.array(transformed_corners)

        # The frame should remain unchanged, so do not modify it here
        # This ensures that the obstacle's origin (frame) stays fixed
