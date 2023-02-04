

def find_slope(points_input):
    slope = ((points_input[1][1]) - (points_input[0][1])) / ((points_input[1][0]) - (points_input[0][0]))
    return slope

def line_contains_point(points_input, point_desired, slope)
    y = point_desired[1] - points_input[0][1]
    x = slope * (point_desired[0] - points_input[0][0]
    if y == x:
        return True
    return False