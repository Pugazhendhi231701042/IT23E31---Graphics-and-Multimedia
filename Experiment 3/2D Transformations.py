import matplotlib.pyplot as plt
import numpy as np

# ---------------- Functions for Transformations -----------------
def translate(vertices, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    ones = np.ones((len(vertices), 1))
    points = np.hstack([vertices, ones])
    transformed = (T @ points.T).T
    return transformed[:, :2]

def scale(vertices, sx, sy):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    ones = np.ones((len(vertices), 1))
    points = np.hstack([vertices, ones])
    transformed = (S @ points.T).T
    return transformed[:, :2]

def rotate(vertices, angle_deg):
    angle = np.radians(angle_deg)
    R = np.array([[np.cos(angle), -np.sin(angle), 0],
                  [np.sin(angle),  np.cos(angle), 0],
                  [0, 0, 1]])
    ones = np.ones((len(vertices), 1))
    points = np.hstack([vertices, ones])
    transformed = (R @ points.T).T
    return transformed[:, :2]

# ---------------- Plot Function -----------------
def plot_shape(vertices, title):
    vertices = np.vstack([vertices, vertices[0]])  # close shape
    plt.plot(vertices[:,0], vertices[:,1], marker='o')
    plt.title(title)
    plt.grid(True)

# ---------------- Main Program -----------------
if __name__ == "__main__":
    # Example shape: triangle
    triangle = np.array([[0,0], [2,0], [1,2]])

    plt.figure(figsize=(12,4))

    # Original
    plt.subplot(1,3,1)
    plot_shape(triangle, "Original Triangle")

    # Translated
    translated = translate(triangle, tx=3, ty=1)
    plt.subplot(1,3,2)
    plot_shape(translated, "Translated Triangle")

    # Scaled and Rotated
    scaled = scale(triangle, sx=2, sy=0.5)
    rotated = rotate(scaled, angle_deg=45)
    plt.subplot(1,3,3)
    plot_shape(rotated, "Scaled & Rotated Triangle")

    plt.show()
