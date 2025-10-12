import numpy as np
import matplotlib.pyplot as plt

def draw_shape(points, label, color):
    """Draws a closed 2D shape."""
    # Append the first point to close the shape
    x, y = zip(*points)
    x += (x[0],)
    y += (y[0],)
    plt.plot(x, y, color=color, label=label)

def apply_transform(points, matrix):
    """Applies a 3x3 homogeneous transformation matrix to a list of (x, y) points."""
    transformed = []
    for x, y in points:
        # Convert (x, y) to homogeneous vector [x, y, 1]
        vec = np.array([x, y, 1])
        # Apply transformation: result = matrix @ vec
        result = matrix @ vec
        # Convert back to Cartesian coordinates (result[0], result[1])
        transformed.append((result[0], result[1]))
    return transformed

def translate(points, tx, ty):
    """Returns the translation transformation matrix and applies it."""
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    return apply_transform(points, T)

def scale(points, sx, sy):
    """Returns the scaling transformation matrix and applies it."""
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    return apply_transform(points, S)

def rotate(points, angle_deg):
    """Returns the rotation transformation matrix and applies it (around origin)."""
    angle_rad = np.radians(angle_deg)
    R = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                  [np.sin(angle_rad), np.cos(angle_rad), 0],
                  [0, 0, 1]])
    return apply_transform(points, R)

# Main Execution
triangle = [(0, 0), (100, 0), (50, 80)] # Original triangle vertices

# Transformations
translated = translate(triangle, 120, 50)
scaled = scale(triangle, 1.5, 1.5)
rotated = rotate(triangle, 45) # 45 degrees rotation

# Plotting
plt.figure(figsize=(8, 8))
draw_shape(triangle, "Original", 'blue')
draw_shape(translated, "Translated", 'green')
draw_shape(scaled, "Scaled", 'orange')
draw_shape(rotated, "Rotated", 'red')

plt.title("2D Transformations")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis("equal") # Ensure equal scaling for correct visualization
plt.show()
