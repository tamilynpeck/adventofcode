import pytest
from utils import read_txt
from day6 import Day6

test_data = ""

def test_day6():
    data = read_txt(test_data)
    program = Day6(data)

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
    program = Day6(data)

    result = program.test()

    assert result == expected
