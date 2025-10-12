import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def draw_edges(ax, vertices, edges, color='b'):
    """Draws the edges of a 3D object on a matplotlib 3D axis."""
    lines = [(vertices[start], vertices[end]) for start, end in edges]
    ax.add_collection3d(Line3DCollection(lines, colors=color, linewidths=1.5))

def translation_matrix(tx, ty, tz):
    """Creates a 4x4 translation matrix."""
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

def scaling_matrix(sx, sy, sz):
    """Creates a 4x4 scaling matrix."""
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])

def rotation_matrix_z(angle):
    """Creates a 4x4 rotation matrix around the Z-axis (angle in degrees)."""
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([[c, -s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def apply_transform(vertices, matrix):
    """Applies a 4x4 homogeneous transformation matrix to a list of (x, y, z) vertices."""
    transformed = []
    for v in vertices:
        # Convert (x, y, z) to homogeneous vector [x, y, z, 1]
        vec = np.array([*v, 1])
        # Apply transformation: result = matrix @ vec
        result = matrix @ vec
        # Convert back to Cartesian coordinates (first 3 elements)
        transformed.append(result[:3])
    return transformed

# Define Cube (unit cube at origin)
vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
            (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), # Bottom face
         (4, 5), (5, 6), (6, 7), (7, 4), # Top face
         (0, 4), (1, 5), (2, 6), (3, 7)] # Connecting edges

# Create Transformation Matrices
# T = Translation by (2, 2, 0)
T = translation_matrix(2, 2, 0) 
# S = Scaling by (1.5, 1.5, 1.5)
S = scaling_matrix(1.5, 1.5, 1.5)
# R = Rotation by 45 degrees around Z-axis
R = rotation_matrix_z(45)

# Combined Transformation (order matters: R then S then T)
# The order in the problem is T @ S @ R
Combined_Matrix = T @ S @ R

# Apply transformation
transformed_vertices = apply_transform(vertices, Combined_Matrix)

# Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw cubes
draw_edges(ax, vertices, edges, 'blue')         # Original cube
draw_edges(ax, transformed_vertices, edges, 'red') # Transformed cube

# Set limits and labels
all_coords = np.array(vertices + transformed_vertices)
max_range = np.array([all_coords[:, 0].max()-all_coords[:, 0].min(),
                      all_coords[:, 1].max()-all_coords[:, 1].min(),
                      all_coords[:, 2].max()-all_coords[:, 2].min()]).max() / 2.0
mid_x, mid_y, mid_z = all_coords.mean(axis=0)
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.set_title("3D Transformation of Cube (Original: Blue, Transformed: Red)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1]) 
plt.show()
