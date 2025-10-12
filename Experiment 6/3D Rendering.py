import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define the 8 vertices of a unit cube
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                     [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

# Define the 6 faces (quadrilaterals) using indices of the vertices array
# Each list represents one face
faces_indices = [
    [0, 1, 2, 3], # Bottom
    [4, 5, 6, 7], # Top
    [0, 1, 5, 4], # Front
    [2, 3, 7, 6], # Back
    [1, 2, 6, 5], # Right
    [4, 7, 3, 0]  # Left
]

# Convert index list to actual coordinates for Poly3DCollection
faces = [[vertices[j] for j in indices] for indices in faces_indices]

# Assign a unique color for each face (Flat Shading)
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'orange']

# GUI Setup and Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D collection with faces, colors, and edges
poly3d = Poly3DCollection(faces, facecolors=colors, edgecolors='black', linewidths=1)
ax.add_collection3d(poly3d)

# Set axes limits (from 0 to 1 for a unit cube)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Cube with Flat Shading')

# Ensure the cube looks like a cube (equal aspect ratio)
ax.set_box_aspect([1, 1, 1]) 

plt.show()
