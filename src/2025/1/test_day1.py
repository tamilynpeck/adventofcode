import pytest
from utils import read_txt
from day1 import Day1, move_dial


test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_part_one():
    data = read_txt(test_data)
    program = Day1(data)

    result = program.solve_part_one()

    assert result == 3


def test_part_two():
    data = read_txt(test_data)
    program = Day1(data)

    result = program.solve_part_two()

    assert result == 6


@pytest.mark.parametrize(
    "i,rotation,expected_i,expected_pass_zero_count",
    [
        (50, "L68", 82, 1),
        (82, "L30", 52, 0),
        (52, "R48", 0, 1),
        (0, "L5", 95, 0),
        (95, "R60", 55, 1),
        (55, "L55", 0, 1),
        (0, "L1", 99, 0),
        (99, "L99", 0, 1),
        (0, "R14", 14, 0),
        (14, "L82", 32, 1),
        (0, "R100", 0, 1),
        (0, "R200", 0, 2),
        (0, "L100", 0, 1),
        (0, "L200", 0, 2),
        (50, "R155", 5, 2),
        (55, "L155", 0, 2),
    ],
)
def test_program_function(i, rotation, expected_i, expected_pass_zero_count):
    new_i, pass_zero_count = move_dial(i, rotation)

    assert new_i == expected_i
    assert pass_zero_count == expected_pass_zero_count
