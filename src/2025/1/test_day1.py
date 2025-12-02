import pytest
from utils import read_txt
from day1 import Day1


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


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day1(data)

#     result = program.test(line)

#     assert result == expected
