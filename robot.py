import roboticstoolbox as rtb
from finger import Finger
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from Object import Obstacle
class Robot:
    
    def __init__(self):
        # Pre-defined robot coordinates
        self.finger1 = Finger("Finger1", base=(0, 0, 0))
        self.finger2 = Finger("Finger2", base=(0, 2, 3))
        self.finger3 = Finger("Finger3", base=(0, -2, 3))
    
    def modifyFinger(self, fingerNo, q):
        if fingerNo == 1:
            self.finger1.adjustPosition(q)
        elif fingerNo == 2:
            self.finger2.adjustPosition(q)
        elif fingerNo == 3:
            self.finger3.adjustPosition(q)
        else:
            print("Invalid finger number")

    def plot_layer(self, ax):
        baseR1 = self.finger1.base
        baseR2 = self.finger2.base
        baseR3 = self.finger3.base

        def plot_finger(base, color, q):
            # Plot the base
            point1 = np.array(base)
            point2 = np.array([base[0] + np.cos(q[0]), base[1] , base[2] + np.sin(q[0])])
            point3 = np.array([point2[0] + np.cos(q[0] + q[1]), point2[1] , point2[2] + np.sin(q[0] + q[1])])

            points = np.array([point1, point2, point3])
            ax.plot(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.set_title('Robot Plot with Connected 3D Points')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_xlim([-2, 2])
            ax.set_ylim([-2, 2])
            ax.set_zlim([0, 4])
        
        plot_finger(baseR1, 'red', self.finger1.robot.q[:2])
        plot_finger(baseR2, 'green', self.finger2.robot.q[:2])
        plot_finger(baseR3, 'blue', self.finger3.robot.q[:2])

        # Show the plot
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        baseR1 = self.finger1.base
        baseR2 = self.finger2.base
        baseR3 = self.finger3.base

        def plot_finger(base, color, q=[np.pi/4,0]):
            # Plot the base
            point1 = np.array(base)
            point2 = np.array([base[0] + np.cos(q[0]), base[1] , base[2] + np.sin(q[0])])
            point3 = np.array([point2[0] + np.cos(q[0] + q[1]), point2[1] , point2[2] + np.sin(q[0] + q[1])])

            points = np.array([point1, point2, point3])
            ax.plot(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.set_title('Robot Plot with Connected 3D Points')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_xlim([-0.2, 2])
            ax.set_ylim([-2, 2])
            ax.set_zlim([-0.2, 4])
        
        plot_finger(baseR1, 'red', self.finger1.robot.q[:2])
        plot_finger(baseR2, 'green', self.finger2.robot.q[:2])
        plot_finger(baseR3, 'blue', self.finger3.robot.q[:2])

        # Show the plot
        plt.show()

    def forward_kinematics(self, fingerNo):
        # Implement forward kinematics for the robot
        if fingerNo == 1:
            return self.finger1.forward_kinematics()
        elif fingerNo == 2:
            return self.finger2.forward_kinematics()
        elif fingerNo == 3:
            return self.finger3.forward_kinematics()
        else:
            print("Invalid")
    
    def inverse_kinematics(self, T, fingerNo):
        # Implement inverse kinematics for the robot
        if fingerNo == 1:
            return self.finger1.inverse_kinematics(T)
        elif fingerNo == 2:
            return self.finger2.inverse_kinematics(T)
        elif fingerNo == 3:
            return self.finger3.inverse_kinematics(T)
        else:
            print("Invalid")

    def plot_with_sliders(self, qs=[[0, 0], [0, 0], [0, 0]]):
        # Create a new figure for the plot
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        baseR1 = self.finger1.base
        baseR2 = self.finger2.base
        baseR3 = self.finger3.base

        # This function will plot the fingers based on the current joint angles
        def plot_finger(base, color, q):
            # Plot the base
            point1 = np.array(base)
            point2 = np.array([base[0] + np.sin(q[0]), base[1], base[2] + np.cos(q[0])])
            point3 = np.array([point2[0] + np.sin(q[0] + q[1]), point2[1], point2[2] + np.cos(q[0] + q[1])])

            points = np.array([point1, point2, point3])
            ax.plot(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=color)
            ax.set_title('Robot Plot with Connected 3D Points')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_xlim([-0.2, 2])
            ax.set_ylim([-2, 2])
            ax.set_zlim([-0.2, 4])
        
        # Initial plot for all three fingers
        plot_finger(baseR1, 'red', qs[0])
        plot_finger(baseR2, 'green', qs[1])
        plot_finger(baseR3, 'blue', qs[2])

        # Define sliders for the joint angles (q[0] and q[1] for each finger)
        ax_slider1_1 = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for first finger, q[0]
        ax_slider1_2 = plt.axes([0.2, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for first finger, q[1]
        
        ax_slider2_1 = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for second finger, q[0]
        ax_slider2_2 = plt.axes([0.2, 0.14, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for second finger, q[1]
        
        ax_slider3_1 = plt.axes([0.2, 0.18, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for third finger, q[0]
        ax_slider3_2 = plt.axes([0.2, 0.22, 0.65, 0.03], facecolor='lightgoldenrodyellow')  # Slider for third finger, q[1]

        # Create sliders
        slider1_1 = Slider(ax_slider1_1, 'Finger 1 q[0]', -np.pi, np.pi, valinit=qs[0][0])
        slider1_2 = Slider(ax_slider1_2, 'Finger 1 q[1]', -np.pi, np.pi, valinit=qs[0][1])
        
        slider2_1 = Slider(ax_slider2_1, 'Finger 2 q[0]', -np.pi, np.pi, valinit=qs[1][0])
        slider2_2 = Slider(ax_slider2_2, 'Finger 2 q[1]', -np.pi, np.pi, valinit=qs[1][1])
        
        slider3_1 = Slider(ax_slider3_1, 'Finger 3 q[0]', -np.pi, np.pi, valinit=qs[2][0])
        slider3_2 = Slider(ax_slider3_2, 'Finger 3 q[1]', -np.pi, np.pi, valinit=qs[2][1])

        # Update function for the sliders
        def update(val):
            # Get the new values from the sliders
            q1 = [slider1_1.val, slider1_2.val]
            q2 = [slider2_1.val, slider2_2.val]
            q3 = [slider3_1.val, slider3_2.val]
            
            # Clear the plot and replot with the updated joint angles
            ax.cla()
            plot_finger(baseR1, 'red', q1)
            plot_finger(baseR2, 'green', q2)
            plot_finger(baseR3, 'blue', q3)
            fig.canvas.draw_idle()

        # Link the update function to all the sliders
        slider1_1.on_changed(update)
        slider1_2.on_changed(update)
        slider2_1.on_changed(update)
        slider2_2.on_changed(update)
        slider3_1.on_changed(update)
        slider3_2.on_changed(update)

        # Show the plot with sliders
        plt.show()