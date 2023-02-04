import pytest


@pytest.mark.parametrize("points_inputs, expected", [(((1, 2), (2, 6)), 4)])
def test_find_slope(points_inputs, expected):
    from line_equation import find_slope
    answer = find_slope(points_inputs)
    assert answer == expected


@pytest.mark.parametrize("points_in, point_desired, slope, expected",
                         [(((1, 2), (2, 6)), (2, 6), 4, True),
                          (((3, 2), (7, 10)), (2, 6), 4, False)])
def test_line_contains_point(points_in, point_desired, slope, expected):
    from line_equation import line_contains_point
    answer = line_contains_point(points_in, point_desired, slope)
    assert answer == expected


@pytest.mark.parametrize("points_input, x_value, slope, expected",
                         [(((1, 2), (2, 4)), 12, 2, 24)])
def test_find_y(points_input, x_value, slope, expected):
    from line_equation import find_y
    answer = find_y(points_input, x_value, slope)
    assert answer == expected
