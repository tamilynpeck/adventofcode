import pytest
from utils import read_txt
from day16 import Day16

test_data = """>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v.."""


def test_day16():
    data = read_txt(test_data)
    program = Day16(data)

    result = program.solve_part_one()

    assert result == 46


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day16(data)

#     result = program.test(line)

#     assert result == expected
