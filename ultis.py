def rectangle_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)


def line_rectangle_collision(line, rect):
    (x1, y1), (x2, y2) = line
    rx, ry, rw, rh = rect
    
    rect_corners = [
        (rx, ry), (rx + rw, ry),      # Top-left to top-right
        (rx + rw, ry + rh), (rx, ry + rh)  # Bottom-right to bottom-left
    ]
    
    # Define rectangle edges as pairs of points
    rect_edges = [
        (rect_corners[0], rect_corners[1]),  # Top edge
        (rect_corners[1], rect_corners[2]),  # Right edge
        (rect_corners[2], rect_corners[3]),  # Bottom edge
        (rect_corners[3], rect_corners[0])   # Left edge
    ]
    
    # Helper function to check if two lines (p1, p2) and (q1, q2) intersect
    def do_intersect(p1, p2, q1, q2):
        # Calculate the direction of the points
        def direction(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        
        d1 = direction(q1, q2, p1)
        d2 = direction(q1, q2, p2)
        d3 = direction(p1, p2, q1)
        d4 = direction(p1, p2, q2)

        # General case
        if d1 * d2 < 0 and d3 * d4 < 0:
            return True
        # Special case when points are collinear
        if d1 == 0 and on_segment(q1, q2, p1): return True
        if d2 == 0 and on_segment(q1, q2, p2): return True
        if d3 == 0 and on_segment(p1, p2, q1): return True
        if d4 == 0 and on_segment(p1, p2, q2): return True
        return False

    # Helper function to check if point p lies on segment ab
    def on_segment(a, b, p):
        return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    
    # Check intersection between the line and each rectangle edge
    for edge in rect_edges:
        if do_intersect((x1, y1), (x2, y2), edge[0], edge[1]):
            return True
    return False


def line_rectangle_collision_point(line, rect):
    # line is defined by two points (x1, y1) and (x2, y2)
    (x1, y1), (x2, y2) = line
    # rect is defined by its top-left corner (rx, ry), width (rw), and height (rh)
    rx, ry, rw, rh = rect
    
    # Define the four corners of the rectangle
    rect_corners = [
        (rx, ry), (rx + rw, ry),      # Top-left to top-right
        (rx + rw, ry + rh), (rx, ry + rh)  # Bottom-right to bottom-left
    ]
    
    # Define rectangle edges as pairs of points
    rect_edges = [
        (rect_corners[0], rect_corners[1]),  # Top edge
        (rect_corners[1], rect_corners[2]),  # Right edge
        (rect_corners[2], rect_corners[3]),  # Bottom edge
        (rect_corners[3], rect_corners[0])   # Left edge
    ]
    
    # Helper function to find the intersection point of two line segments (p1, p2) and (q1, q2)
    def get_intersection_point(p1, p2, q1, q2):
        # Calculate the direction and denominator for the intersection formula
        A1 = p2[1] - p1[1]
        B1 = p1[0] - p2[0]
        C1 = A1 * p1[0] + B1 * p1[1]
        
        A2 = q2[1] - q1[1]
        B2 = q1[0] - q2[0]
        C2 = A2 * q1[0] + B2 * q1[1]
        
        denominator = A1 * B2 - A2 * B1
        
        # If denominator is 0, the lines are parallel (no intersection)
        if denominator == 0:
            return None
        
        # Calculate intersection point
        x = (B2 * C1 - B1 * C2) / denominator
        y = (A1 * C2 - A2 * C1) / denominator
        
        # Check if the intersection point lies on both segments
        if on_segment(p1, p2, (x, y)) and on_segment(q1, q2, (x, y)):
            return (x, y)
        return None

    # Helper function to check if point p lies on segment ab
    def on_segment(a, b, p):
        return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

    # Check intersection between the line and each rectangle edge
    for edge in rect_edges:
        intersection = get_intersection_point((x1, y1), (x2, y2), edge[0], edge[1])
        if intersection:
            return intersection  # Return the first collision point found

    return None  # No collision point found


