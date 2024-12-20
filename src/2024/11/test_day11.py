import pytest
from utils import read_txt
from day11 import Day11


test_data = "125 17"


def test_part_one_six():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_one(blinks=6)

    assert result == 22


def test_part_one():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_one()

    assert result == 55312


def test_part_two():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_two()

    assert result


@pytest.mark.parametrize(
    "line,expected",
    [
        ({125: 1, 17: 1}, {253000: 1, 1: 1, 7: 1}),
        (
            {
                1036288: 1,
                7: 1,
                2: 1,
                20: 1,
                24: 1,
                4048: 1,
                1: 1,
                8096: 1,
                28: 1,
                67: 1,
                60: 1,
                32: 1,
            },
            {
                2097446912: 1,
                14168: 1,
                4048: 1,
                2: 4,
                0: 2,
                4: 1,
                40: 1,
                48: 1,
                2024: 1,
                80: 1,
                96: 1,
                8: 1,
                6: 2,
                7: 1,
                3: 1,
            },
        ),
    ],
)
def test_program_function(line, expected):
    result = Day11.blink(line)

    assert result == expected
