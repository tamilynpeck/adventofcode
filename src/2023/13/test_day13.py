import pytest
from utils import read_txt
from day13 import Day13

test_data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_day13():
    data = read_txt(test_data)
    program = Day13(data)

    result = program.solve_part_one()

    assert result == 405


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day13(data)

#     result = program.test()

#     assert result == expected
