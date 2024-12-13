import pytest
from utils import read_txt
from day6 import Day6


test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_part_one():
    data = read_txt(test_data)
    program = Day6(data)

    result = program.solve_part_one()

    assert result == 41


def test_part_two():
    data = read_txt(test_data)
    program = Day6(data)

    result = program.solve_part_two()

    assert result == 6
