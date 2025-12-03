import pytest
from utils import read_txt
from day3 import Day3


test_data = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part_one():
    data = read_txt(test_data)
    program = Day3(data)

    result = program.solve_part_one()

    assert result == 357


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day3(data)

#     result = program.solve_part_two()

#     assert result == 0


@pytest.mark.parametrize(
    "line,expected",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day3(data)

    result = program.find_maximum_joltage(line)

    assert result == expected
