import matplotlib.pyplot as plt

def draw_ellipse_points(xc, yc, x, y, points):
    # 4-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
    ])

def midpoint_ellipse(xc, yc, rx, ry):
    points = []
    x, y = 0, ry

    # Initial decision parameters
    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    while dx < dy:
        draw_ellipse_points(xc, yc, x, y, points)
        if p1 < 0:
            x += 1
            dx += two_ry2
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx += two_ry2
            dy -= two_rx2
            p1 += dx - dy + ry2

    # Region 2
    p2 = (ry2) * ((x + 0.5) ** 2) + (rx2) * ((y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        draw_ellipse_points(xc, yc, x, y, points)
        if p2 > 0:
            y -= 1
            dy -= two_rx2
            p2 += rx2 - dy
        else:
            y -= 1
            x += 1
            dx += two_ry2
            dy -= two_rx2
            p2 += dx - dy + rx2

    return points

# ---- Main Program ----
if __name__ == "__main__":
    xc, yc, rx, ry = 50, 50, 40, 20
    ellipse_points = midpoint_ellipse(xc, yc, rx, ry)

    # Extract coordinates
    x_coords, y_coords = zip(*ellipse_points)

    # Plot the ellipse
    plt.plot(x_coords, y_coords, 'go')   # green dots
    plt.title("Midpoint Ellipse Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()
