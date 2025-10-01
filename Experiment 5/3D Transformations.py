import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# ---------------- Draw 3D Object -----------------
def draw(ax, vertices, edges, color):
    ax.add_collection3d(Line3DCollection([(vertices[i], vertices[j]) for i,j in edges], colors=color))

# ---------------- Transformation Matrices -----------------
def translate(tx, ty, tz):
    return np.array([[1,0,0,tx],
                     [0,1,0,ty],
                     [0,0,1,tz],
                     [0,0,0,1]])

def scale(sx, sy, sz):
    return np.array([[sx,0,0,0],
                     [0,sy,0,0],
                     [0,0,sz,0],
                     [0,0,0,1]])

def rotz(angle_deg):
    r = np.radians(angle_deg)
    return np.array([[np.cos(r), -np.sin(r),0,0],
                     [np.sin(r),  np.cos(r),0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

# ---------------- Apply Transformation -----------------
def apply(vertices, matrix):
    return [(matrix @ np.array([*v,1]))[:3] for v in vertices]

# ---------------- Main Program -----------------
if __name__ == "__main__":
    # Cube vertices and edges
    vertices = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),
                (0,0,1),(1,0,1),(1,1,1),(0,1,1)]
    edges = [(0,1),(1,2),(2,3),(3,0),
             (4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]

    # Transformation: translate, scale, rotate
    M = translate(2,2,0) @ scale(1.5,1.5,1.5) @ rotz(45)
    transformed_vertices = apply(vertices, M)

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    draw(ax, vertices, edges, 'blue')           # original cube
    draw(ax, transformed_vertices, edges, 'red') # transformed cube
    ax.set_title("3D Transformations")
    plt.show()
