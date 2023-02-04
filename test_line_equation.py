import pytest

@pytest.mark.parametrize("points_inputs, expected", [(((1, 2),(2, 6)), 4)])
def test_find_slope(point_inputs, expected):
    from line_equation import find_slope
    answer = find_slope(points_inputs)
    assert answer == expected


@pytest.mark.parametrize("points_in, point_desired, expected",
[(((1, 2),(2, 6)), (2, 6), True)])
def test_line_contains_point(point_in, point_desired, expected):
    from line_equation import test_line_contains_point
    answer = test_line_contains_points(point_in, point_desired)
    assert answer == expected    