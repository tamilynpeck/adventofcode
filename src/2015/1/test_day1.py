import pytest
from utils import read_txt
from day1 import Day1


@pytest.mark.parametrize(
    "line,expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part_one_examples(line, expected):
    data = read_txt(line)
    program = Day1(data)

    result = program.solve_part_one()

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_part_two_examples(line, expected):
    data = read_txt(line)
    program = Day1(data)

    result = program.solve_part_two()

    assert result == expected
