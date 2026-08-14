import pytest
from utils import read_txt
from day5 import Day5


test_data = """"""


def test_part_one():
    data = read_txt(test_data)
    program = Day5(data)

    result = program.solve_part_one()

    assert result == 0


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day5(data)

#     result = program.solve_part_two()

#     assert result == 0


@pytest.mark.parametrize(
    "line,expected",
    [
        ("line", "expected"),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day5(data)

    result = program.test(line)

    assert result == expected
