import pytest
from utils import read_txt
from day17 import Day17


test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


def test_part_one():
    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == "4,6,3,5,6,3,5,2,1,0"


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day17(data)

#     result = program.solve_part_two()

#     assert result == 0


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day17(data)

#     result = program.test(line)

#     assert result == expected
