# Solutions to exercise 1.2 on Forward Kinematics
# Using the robotic toolbox

from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH

# Link lengths
L1 = 0.5

# Define the robot using Denavit-Hartenberg parameters
L = [
	RevoluteMDH( alpha=0,     a=0,  d=0,     qlim=[-pi, pi]),  # Rotational
	PrismaticMDH(alpha=pi/2,  a=L1, theta=0, qlim=[-1, 1]),    # Translational
	RevoluteMDH( alpha=pi/2,  a=0,  d=0,     qlim=[-pi, pi]),  # Rotational
]

# Create the robot
threeDOF = DHRobot(L, name="ThreeDOF-RRR")
print(threeDOF)
# Visualize the robot and test movements

threeDOF.teach([0, 0, 0])