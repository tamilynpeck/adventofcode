import pytest
from utils import read_txt
from day2 import Day2

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_part_one():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_one()

    assert result == 2


def test_part_two():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_two()

    assert result == 4
