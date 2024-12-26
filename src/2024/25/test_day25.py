import pytest
from utils import read_txt
from day25 import Day25


test_data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def test_create():
    data = read_txt(test_data)
    program = Day25(data)

    assert [0, 5, 3, 4, 3] in program.locks
    assert [1, 2, 0, 5, 3] in program.locks
    assert [5, 0, 2, 1, 3] in program.keys
    assert [4, 3, 4, 0, 2] in program.keys
    assert [3, 0, 2, 0, 1] in program.keys


def test_part_one():
    data = read_txt(test_data)
    program = Day25(data)

    result = program.solve_part_one()

    assert result == 3


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day25(data)

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
#     program = Day25(data)

#     result = program.test(line)

#     assert result == expected
