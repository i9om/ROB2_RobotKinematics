# Solutions to exercise 2 on Forward Kinematics
# Using the robotic toolbox

from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH
#Use this - I
import matplotlib
matplotlib.use('TkAgg')  # or 'TkAgg' if Qt5Agg doesn't work

# Define the robot using Denavit-Hartenberg parameters
L = [
	RevoluteMDH( alpha=0,  a=0,   d=0.342,   qlim=[-pi, pi]),  # Rotational
	RevoluteMDH( alpha=0,  a=0.325, d=0,     qlim=[-pi, pi]),  # Rotational
	PrismaticMDH(alpha=0,  a=0.275, theta=0, offset = -0.165, qlim=[-1, 1]),    # Translational
	RevoluteMDH( alpha=0,  a=0,   d=0,     qlim=[-pi, pi]),  # Rotational
]

# Create the robot
Scara = DHRobot(L, name="Scara")
print(Scara)
# Visualize the robot and test movements

Scara.teach([0, 0, 0, 0])