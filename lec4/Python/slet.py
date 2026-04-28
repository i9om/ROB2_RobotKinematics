from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH
import matplotlib

matplotlib.use('TkAgg')  # or 'Qt5Agg- if  doesn't work

L1 = 1
L2 = 1

# Define the robot using Denavit-Hartenberg parameters
L = [
	RevoluteMDH( alpha=0,  a=0,  d=0),  # Rotational
	RevoluteMDH( alpha=0,  a=L1, d=0),  # Rotational
	RevoluteMDH(alpha=0,  a=L2, d=0),  # Rotational
]

# Create the robot
ThreeDOF = DHRobot(L, name="3DOF")

# Visualize the robot and test movements

ThreeDOF.teach([0, 0, 0])