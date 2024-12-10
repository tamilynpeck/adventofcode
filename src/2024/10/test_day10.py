import pytest
from utils import read_txt
from day10 import Day10


test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_part_one():
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 36


def test_part_one_small_1():
    test_data = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 2


def test_part_one_small_2():
    test_data = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 4


def test_part_one_small_3():
    test_data = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 3


def test_part_one_small_4():
    test_data = """0123
1234
8765
9876"""
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_one()

    assert result == 1


def test_part_two():
    data = read_txt(test_data)
    program = Day10(data)

    result = program.solve_part_two()

    assert result == 81


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day10(data)

#     result = program.test(line)

#     assert result == expected
