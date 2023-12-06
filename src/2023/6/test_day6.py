import pytest
from utils import read_txt
from day6 import Day6

test_data = """Time:      7  15   30
Distance:  9  40  200"""


def test_day6():
    data = read_txt(test_data)
    program = Day6(data)

    result = program.solve_part_one()

    assert result == 288


def test_day6():
    data = read_txt(test_data)
    program = Day6(data)

    result = program.solve_part_two()

    assert result == 71503


@pytest.mark.parametrize(
    "time, record_distance ,expected",
    [(7, 9, 4), (15, 40, 8), (30, 200, 9)],
)
def test_program_function(time, record_distance, expected):
    result = Day6.button_math(time, record_distance)

    assert result == expected
