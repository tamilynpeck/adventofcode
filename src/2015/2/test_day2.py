import pytest
from utils import read_file, read_txt
from day2 import Day2


test_data = """2x3x4
1x1x10"""

def test_part_one():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_one()

    assert result == 58 + 43

@pytest.mark.parametrize(
    "line,expected",
    [
        ((2, 3, 4), 58),
        ((1, 1, 10), 43),
    ],
)
def test_square_feet(line, expected):
    data = read_txt(test_data)
    program = Day2(data)

    result = program.square_feet(*line)

    assert result == expected


def test_part_two():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_two()

    assert result == 34 + 14

@pytest.mark.parametrize(
    "line,expected",
    [
        ((2, 3, 4), 34),
        ((1, 1, 10), 14),
    ],
)
def test_ribbon(line, expected):
    data = read_txt(test_data)
    program = Day2(data)

    result = program.ribbon(*line)

    assert result == expected

def test_solutions():
    data = read_file("input.txt")
    program = Day2(data)
    result = program.solve_part_one()
    assert result == 1588178
    result = program.solve_part_two()
    assert result == 3783758
