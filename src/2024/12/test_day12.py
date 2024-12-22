import pytest
from utils import read_txt
from day12 import Day12


small_test_data = """AAAA
BBCD
BBCC
EEEC"""

small_test_data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_part_one_example_one():
    small_test_data = """AAAA
BBCD
BBCC
EEEC"""
    data = read_txt(small_test_data)
    program = Day12(data)

    result = program.solve_part_one()

    assert result == 140


# def test_part_one_example_two():
#     small_test_data = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO"""
#     data = read_txt(small_test_data)
#     program = Day12(data)

#     result = program.solve_part_one()

#     assert result == 772


# def test_part_one():
#     data = read_txt(test_data)
#     program = Day12(data)

#     result = program.solve_part_one()

#     assert result == 1930


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day12(data)

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
#     program = Day12(data)

#     result = program.test(line)

#     assert result == expected
