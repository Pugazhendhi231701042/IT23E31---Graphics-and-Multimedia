import matplotlib.pyplot as plt
import numpy as np
from collections import deque

width, height = 300, 300
canvas = np.ones((height, width, 3), dtype=np.uint8) * 255 # White canvas

def bresenham_line(x1, y1, x2, y2):
    """Draws a line on the canvas using Bresenham's algorithm (Black line)."""
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2
        while x != x2:
            canvas[y, x] = [0, 0, 0] # Set pixel to black
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            canvas[y, x] = [0, 0, 0] # Set pixel to black
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    canvas[y, x] = [0, 0, 0] # Final point

def draw_polygon(vertices):
    """Draws a polygon by connecting its vertices with lines."""
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        bresenham_line(x1, y1, x2, y2)

def flood_fill_iter(x, y, target_color, fill_color):
    """Iterative Flood-Fill Algorithm using a deque (Breadth-First Search)."""
    target = np.array(target_color, dtype=np.uint8)
    fill = np.array(fill_color, dtype=np.uint8)

    # Check bounds and initial color
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    if not np.array_equal(canvas[y, x], target):
        return

    q = deque([(x, y)])
    
    while q:
        cx, cy = q.popleft()
        
        # Simple bounds check, more rigorous checks are better for real apps
        if cx < 0 or cx >= width or cy < 0 or cy >= height:
            continue
            
        if np.array_equal(canvas[cy, cx], target):
            canvas[cy, cx] = fill_color
            
            # Add neighbors to queue (4-connected)
            q.append((cx + 1, cy))
            q.append((cx - 1, cy))
            q.append((cx, cy + 1))
            q.append((cx, cy - 1))

# Main Execution
vertices = [(50, 50), (250, 50), (200, 200), (100, 250), (50, 150)]
draw_polygon(vertices)

# Fill the polygon: seed point (150, 100), target color white (255, 255, 255), fill color red (255, 0, 0)
flood_fill_iter(150, 100, [255, 255, 255], [255, 0, 0])

plt.imshow(canvas)
plt.title("Polygon Fill using Flood-Fill Algorithm (Iterative)")
plt.axis('off')
plt.show()
