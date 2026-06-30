import numpy as np
import matplotlib.pyplot as plt

# Robotic Arm Link Lengths
L1 = 10
L2 = 10

# Target Point
x = 12
y = 8

# Inverse Kinematics
cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
theta2 = np.arccos(cos_theta2)

theta1 = np.arctan2(y, x) - np.arctan2(
    L2 * np.sin(theta2),
    L1 + L2 * np.cos(theta2)
)

print("Theta1 =", np.degrees(theta1))
print("Theta2 =", np.degrees(theta2))

# Waypoints for Path Planning
path_x = [0, 5, 10, 12]
path_y = [0, 4, 6, 8]

# Plot Path
plt.plot(path_x, path_y, marker='o')
plt.scatter(path_x[0], path_y[0], label="Start Point")
plt.scatter(path_x[-1], path_y[-1], label="End Point")

plt.title("Robotic Arm Path Planning")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.legend()

plt.show()