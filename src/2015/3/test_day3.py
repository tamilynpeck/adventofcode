import pytest
from utils import read_file, read_txt
from day3 import Day3


@pytest.mark.parametrize(
    "line,expected",
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day3(data)

    result = program.solve_part_one()

    assert result == expected

@pytest.mark.parametrize(
    "line,expected",
    [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day3(data)

    result = program.solve_part_two()

    assert result == expected

def test_solutions():
    data = read_file("input.txt")
    program = Day3(data)
    result = program.solve_part_one()
    assert result == 2565
    result = program.solve_part_two()
    assert result == 2639
