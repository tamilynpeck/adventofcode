import pytest
from utils import read_txt
from day18 import Day18


test_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_part_one():
    data = read_txt(test_data)
    program = Day18(data)

    result = program.solve_part_one(size=6, bytes=12)

    assert result == 22


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day18(data)

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
#     program = Day18(data)

#     result = program.test(line)

#     assert result == expected
