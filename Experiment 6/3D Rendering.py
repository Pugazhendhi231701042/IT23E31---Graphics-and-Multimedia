import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# ---------------- Cube vertices -----------------
vertices = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
                     [0,0,1],[1,0,1],[1,1,1],[0,1,1]])

# ---------------- Cube faces -----------------
faces = [[vertices[j] for j in [0,1,2,3]],
         [vertices[j] for j in [4,5,6,7]],
         [vertices[j] for j in [0,1,5,4]],
         [vertices[j] for j in [2,3,7,6]],
         [vertices[j] for j in [1,2,6,5]],
         [vertices[j] for j in [4,7,3,0]]]

# ---------------- Face colors -----------------
colors = ['red','blue','green','yellow','cyan','orange']

# ---------------- Plot -----------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube = Poly3DCollection(faces, facecolors=colors, edgecolors='black')
ax.add_collection3d(cube)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Cube with Flat Shading')
ax.set_box_aspect([1,1,1])  # Equal aspect ratio
plt.show()
