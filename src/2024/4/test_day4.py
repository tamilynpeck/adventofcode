import pytest
from utils import read_txt
from day4 import Day4


test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_part_one():
    data = read_txt(test_data)
    program = Day4(data)

    result = program.solve_part_one()

    assert result == 18


def test_part_two():
    data = read_txt(test_data)
    program = Day4(data)

    result = program.solve_part_two()

    assert result == 9


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day4(data)

#     result = program.test(line)

#     assert result == expected
