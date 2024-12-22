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


def test_part_one_ex_1():
    test_data = """Register A: 0
    Register B: 0
    Register C: 9

    Program: 2,6"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == ""
    assert program.register_b == 1


def test_part_one_ex_2():
    test_data = """Register A: 10
    Register B: 0
    Register C: 0

    Program: 5,0,5,1,5,4"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == "0,1,2"


def test_part_one_ex_3():
    test_data = """Register A: 2024
    Register B: 0
    Register C: 0

    Program: 0,1,5,4,3,0"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == "4,2,5,6,7,7,7,7,3,1,0"
    assert program.register_a == 0


def test_part_one_ex_4():
    test_data = """Register A: 0
    Register B: 29
    Register C: 0

    Program: 1,7"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == ""
    assert program.register_b == 26


def test_part_one_ex_5():
    test_data = """Register A: 0
    Register B: 2024
    Register C: 43690

    Program: 4,0"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_one()

    assert result == ""
    assert program.register_b == 44354


def test_part_two():
    test_data = """Register A: 2024
    Register B: 0
    Register C: 0

    Program: 0,1,5,4,3,0"""

    data = read_txt(test_data)
    program = Day17(data)

    result = program.solve_part_two()

    assert result == 117440


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
