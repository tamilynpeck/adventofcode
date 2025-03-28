import pytest
from utils import read_txt
from day16 import Day16


test_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def test_part_one():
    data = read_txt(test_data)
    program = Day16(data)

    result = program.solve_part_one()

    assert result == 11048


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day16(data)

#     result = program.solve_part_two()

#     assert result == 0


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day16(data)

#     result = program.test(line)

#     assert result == expected
