

def line_equation_driver():
    points_in = ((1, 2), (4, 8))
    point_desired = (2, 4)
    slope = find_slope(points_in)
    does_it = line_contains_point(points_in, point_desired, slope)
    y = find_y(points_in, 5, slope)
    print("{}".format(does_it))
    print("{}".format(y))


def find_slope(points_input):
    slope = (((points_input[1][1]) - (points_input[0][1])) /
             ((points_input[1][0]) - (points_input[0][0])))
    return slope


def line_contains_point(points_input, point_desired, slope):
    y = point_desired[1] - points_input[0][1]
    x = slope * (point_desired[0] - points_input[0][0])
    if y == x:
        return True
    return False


def find_y(points_input, x_value, slope):
    y = slope * (x_value - points_input[0][0]) + points_input[0][1]
    return y


if __name__ == "__main__":
    line_equation_driver()
