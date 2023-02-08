import pytest


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"),
                          (45, "Borderline Low"),
                          (20, "Low")
                          ])
def test_HDL_analysis(HDL_input, expected):
    from bloodcalculator import HDL_analysis
    # Arrange
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(100, "Normal"),
                          (145, "Borderline High"),
                          (175, "High"),
                          (200, "Very High")
                          ])
def test_LDL_analysis(LDL_input, expected):
    from bloodcalculator import LDL_analysis
    answer = LDL_analysis(LDL_input)
    assert answer == expected
