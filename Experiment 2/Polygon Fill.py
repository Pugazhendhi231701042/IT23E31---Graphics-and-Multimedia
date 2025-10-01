import matplotlib.pyplot as plt
import numpy as np

# ---------------- Canvas -----------------
width, height = 100, 100
canvas = np.zeros((height, width))  # 0 = background, 1 = boundary, 2 = fill

# ---------------- Bresenham Line -----------------
def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    x, y = x1, y1

    while True:
        canvas[y, x] = 1
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

# ---------------- Draw Polygon -----------------
def draw_polygon(vertices):
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1)%n]
        bresenham_line(x1, y1, x2, y2)

# ---------------- Flood Fill -----------------
def flood_fill(x, y):
    if canvas[y, x] != 0:
        return
    canvas[y, x] = 2
    flood_fill(x+1, y)
    flood_fill(x-1, y)
    flood_fill(x, y+1)
    flood_fill(x, y-1)

# ---------------- Main -----------------
polygon = [(20,20), (80,20), (70,70), (30,60)]
draw_polygon(polygon)
flood_fill(50, 30)

plt.imshow(canvas, cmap='viridis', origin='lower')
plt.title("Polygon with Flood Fill")
plt.show()
