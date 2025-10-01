import matplotlib.pyplot as plt

# Edges identifiers
LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

# Check if a point is inside a given edge
def inside(p, edge, window):
    x, y = p
    xmin, xmax, ymin, ymax = window
    if edge == LEFT:   return x >= xmin
    if edge == RIGHT:  return x <= xmax
    if edge == BOTTOM: return y >= ymin
    if edge == TOP:    return y <= ymax

# Find intersection of a line segment with an edge
def intersect(p1, p2, edge, window):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax, ymin, ymax = window

    if edge == LEFT:
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == RIGHT:
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == BOTTOM:
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == TOP:
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
    return (x, y)

# Sutherland-Hodgman Polygon Clipping
def sutherland_hodgman(polygon, window):
    output = polygon
    for edge in [LEFT, RIGHT, BOTTOM, TOP]:
        input_list = output
        output = []
        if not input_list:
            break
        s = input_list[-1]
        for p in input_list:
            if inside(p, edge, window):
                if not inside(s, edge, window):
                    output.append(intersect(s, p, edge, window))
                output.append(p)
            elif inside(s, edge, window):
                output.append(intersect(s, p, edge, window))
            s = p
    return output

# Plot polygon
def plot_polygon(polygon, color, label):
    polygon.append(polygon[0])
    x, y = zip(*polygon)
    plt.plot(x, y, color=color, label=label)

# ---------------- Main -----------------
if __name__ == "__main__":
    polygon = [(50,150), (200,50), (350,150), (350,300), (250,350), (150,300)]
    clip_window = (100, 300, 100, 300)  # xmin, xmax, ymin, ymax

    clipped = sutherland_hodgman(polygon, clip_window)

    plt.figure(figsize=(8,8))
    plot_polygon(polygon.copy(), 'blue', 'Original')
    plot_polygon(clipped.copy(), 'red', 'Clipped')
    # Draw clipping window
    win_rect = [(clip_window[0], clip_window[2]), (clip_window[1], clip_window[2]),
                (clip_window[1], clip_window[3]), (clip_window[0], clip_window[3])]
    plot_polygon(win_rect, 'black', 'Window')
    plt.legend()
    plt.title("Sutherland-Hodgman Polygon Clipping")
    plt.grid(True)
    plt.axis("equal")
    plt.show()