import pytest
from utils import read_txt
from day3 import Day3

test_data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def test_part_one():
    data = read_txt(test_data)
    program = Day3(data)

    result = program.solve_part_one()

    assert result == 161


def test_part_two():
    data = read_txt(test_data)
    program = Day3(data)

    result = program.solve_part_two()

    assert result == 48
