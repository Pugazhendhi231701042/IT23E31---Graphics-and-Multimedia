import matplotlib.pyplot as plt
import numpy as np

# Define clipping edges for easier reading
LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

def inside(p, edge, clip_win):
    """Checks if point p is inside the boundary defined by 'edge' of 'clip_win'."""
    x, y = p
    xmin, xmax, ymin, ymax = clip_win
    if edge == LEFT:
        return x >= xmin
    elif edge == RIGHT:
        return x <= xmax
    elif edge == BOTTOM:
        return y >= ymin
    elif edge == TOP:
        return y <= ymax
    return False

def intersect(p1, p2, edge, clip_win):
    """Calculates the intersection point of the line segment p1-p2 with the clipping edge."""
    xmin, xmax, ymin, ymax = clip_win
    x1, y1 = p1
    x2, y2 = p2
    
    # Avoid division by zero for vertical/horizontal lines
    if x2 - x1 == 0 and (edge == LEFT or edge == RIGHT): return (x1, y1)
    if y2 - y1 == 0 and (edge == BOTTOM or edge == TOP): return (x1, y1)

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

def clip_polygon(polygon, clip_win):
    """Clips the polygon against the rectangular window using Sutherland-Hodgman."""
    output = polygon
    
    # Clip against each of the four edges (Left, Right, Bottom, Top)
    for edge in [LEFT, RIGHT, BOTTOM, TOP]:
        input_list = output
        output = [] # New list for the clipped polygon
        
        if not input_list:
            break

        s = input_list[-1] # Start with the last vertex of the current polygon

        for p in input_list:
            # Case 1: p is inside, s is outside -> Add intersection and p
            if inside(p, edge, clip_win):
                if not inside(s, edge, clip_win):
                    output.append(intersect(s, p, edge, clip_win))
                output.append(p)
            # Case 2: p is outside, s is inside -> Add intersection only
            elif inside(s, edge, clip_win):
                output.append(intersect(s, p, edge, clip_win))
            # Case 3: p and s are outside -> Add nothing
            # Case 4: p and s are inside -> Add p (done in Case 1, as s inside implies no intersection needed)
            
            s = p # Move to the next segment
            
    return output

def draw_polygon(points, color, label):
    """Plots a polygon."""
    # Unzip coordinates and close the loop
    if points:
        x, y = zip(*(points + [points[0]]))
        plt.plot(x, y, color=color, label=label)

# Main Execution
clip_window = (100, 300, 100, 300) # xmin, xmax, ymin, ymax
polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 350), (150, 300)]

clipped_poly = clip_polygon(polygon, clip_window)

plt.figure(figsize=(8, 8))
draw_polygon(polygon, 'blue', "Original Polygon")

# Draw Clipping Window (a rectangle)
clip_rect_points = [
    (clip_window[0], clip_window[2]), 
    (clip_window[1], clip_window[2]),
    (clip_window[1], clip_window[3]), 
    (clip_window[0], clip_window[3])
]
draw_polygon(clip_rect_points, 'black', "Clipping Window")

draw_polygon(clipped_poly, 'red', "Clipped Polygon")

plt.legend()
plt.title("Polygon Clipping using Sutherland-Hodgman Algorithm")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis("equal")
plt.show()
