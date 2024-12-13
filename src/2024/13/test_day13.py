import pytest
from utils import read_txt
from day13 import Day13


test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_part_one():
    data = read_txt(test_data)
    program = Day13(data)

    result = program.solve_part_one()

    assert result == 480


def test_part_two():
    data = read_txt(test_data)
    program = Day13(data)

    result = program.solve_part_two()

    assert result == 875318608908


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400""",
            280,
        ),
        (
            """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176""",
            None,
        ),
        (
            """Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450""",
            200,
        ),
        (
            """Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
            None,
        ),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day13(data)

    result = program.evaluate_claw_machine(program.data[0])

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400""",
            None,
        ),
        (
            """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176""",
            459236326669,
        ),
        (
            """Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450""",
            None,
        ),
        (
            """Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
            416082282239,
        ),
    ],
)
def test_program_function_part_two(line, expected):
    data = read_txt(line)
    program = Day13(data)

    claw = program.data[0]
    claw.part_two_update()

    result = program.evaluate_claw_machine(claw)

    assert result == expected
