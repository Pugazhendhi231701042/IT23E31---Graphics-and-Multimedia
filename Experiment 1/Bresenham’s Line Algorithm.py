import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))  # Store point
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

# ---- Main Program ----
if __name__ == "__main__":
    x1, y1 = 2, 3
    x2, y2 = 15, 10
    
    line_points = bresenham_line(x1, y1, x2, y2)

    # Plot the line
    x_coords, y_coords = zip(*line_points)
    plt.plot(x_coords, y_coords, 'ro')   # red dots
    plt.title("Bresenham's Line Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
