import pytest
from utils import read_txt
from day14 import Day14

test_data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_day14():
    data = read_txt(test_data)
    program = Day14(data)

    result = program.solve_part_one()

    assert result == 136


def test_day14_part_two():
    data = read_txt(test_data)
    program = Day14(data)

    result = program.solve_part_two(cycles=10000000)

    assert result == 64


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day14(data)

#     result = program.test(line)

#     assert result == expected
