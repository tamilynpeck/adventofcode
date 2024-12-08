import pytest
from utils import read_txt
from day8 import Day8


test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def test_part_one():
    data = read_txt(test_data)
    program = Day8(data)

    result = program.solve_part_one()

    assert result == 14


def test_part_two():
    data = read_txt(test_data)
    program = Day8(data)

    result = program.solve_part_two()

    assert result == 34


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day8(data)

#     result = program.test(line)

#     assert result == expected
