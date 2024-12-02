import pytest
from utils import read_txt
from day3 import Day3

test_data = ""

def test_day3():
    data = read_txt(test_data)
    program = Day3(data)

    result = program.solve_part_one()

    assert result == 0

@pytest.mark.parametrize(
    "line,expected",
    [
        ("line", "expected"),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day3(data)

    result = program.test(line)

    assert result == expected
