# Solutions to exercise 1.1 on Forward Kinematics
# Using the robotic toolbox

from math import pi

from roboticstoolbox import DHRobot, RevoluteMDH

# Link lengths
L1 = 1
L2 = 1

# Define the robot using Denavit-Hartenberg parameters
L = [
	RevoluteMDH(alpha=0, a=0, d=0),  # Rotational
	RevoluteMDH(alpha=pi/2, a=L1, d=0),  # Rotational
	RevoluteMDH(alpha=0, a=L2, d=0),  # Rotational
]

# Create the robot
threeDOF = DHRobot(L, name="ThreeDOF-RRR")
print(threeDOF)
# Visualize the robot and test movements
threeDOF.teach([0, 0, 0])

