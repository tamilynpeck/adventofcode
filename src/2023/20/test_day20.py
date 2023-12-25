import pytest
from utils import read_txt
from day20 import Day20


def test_day20_first_example():
    test_data = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
    data = read_txt(test_data)
    program = Day20(data)

    result = program.solve_part_one()

    assert result == 32000000


def test_day20_second_example():
    test_data = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
    data = read_txt(test_data)
    program = Day20(data)

    result = program.solve_part_one()

    assert result == 11687500


# @pytest.mark.parametrize(
#     "line,expected",
#     [
#         ("line", "expected"),
#     ],
# )
# def test_program_function(line, expected):
#     data = read_txt(line)
#     program = Day20(data)

#     result = program.test(line)

#     assert result == expected
