import matplotlib.pyplot as plt

def draw_circle_points(xc, yc, x, y, points):
    # 8-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ])

def midpoint_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    p = 1 - r   # Initial decision parameter

    draw_circle_points(xc, yc, x, y, points)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_circle_points(xc, yc, x, y, points)

    return points

# ---- Main Program ----
if __name__ == "__main__":
    xc, yc, r = 50, 50, 30
    circle_points = midpoint_circle(xc, yc, r)

    # Extract coordinates
    x_coords, y_coords = zip(*circle_points)

    # Plot the circle
    plt.plot(x_coords, y_coords, 'bo')   # blue dots
    plt.title("Midpoint Circle Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
    plt.grid(True)
    plt.show()
