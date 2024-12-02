import pytest
from utils import read_txt
from day1 import Day1


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_data_parsing():
    data = read_txt(test_data)
    program = Day1(data)

    assert program.left_list == [3, 4, 2, 1, 3, 3]
    assert program.right_list == [4, 3, 5, 3, 9, 3]


def test_part_one():
    data = read_txt(test_data)
    program = Day1(data)

    result = program.solve_part_one()

    assert result == 11


def test_part_two():
    data = read_txt(test_data)
    program = Day1(data)

    result = program.solve_part_two()

    assert result == 31
