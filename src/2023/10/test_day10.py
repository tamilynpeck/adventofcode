import pytest
from utils import read_txt
from day10 import Day10


def test_day10():
    test_data = """.....
.S-7.
.|.|.
.L-J.
.....
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 4


def test_day10_with_extra_pipes():
    test_data = """.....
.S-7.
.|.|.
.L-J.
.....
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 4


def test_day10_complex_example():
    test_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 8


def test_day10_complex_example_with_extra_pipes():
    test_data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 8


def test_day10_part_two():
    test_data = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_two()

    assert result == 4


def test_day10_part_two_another():
    test_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_two()

    assert result == 10


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day10(data)

#     result = program.test()

#     assert result == expected
