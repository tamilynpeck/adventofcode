import pytest
from utils import read_txt
from day15 import Day15

test_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_day15():
    data = read_txt(test_data)
    program = Day15(data)

    result = program.solve_part_one()

    assert result == 1320


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day15(data)

#     result = program.test(line)

#     assert result == expected
