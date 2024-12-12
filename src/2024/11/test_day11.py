import pytest
from utils import read_txt
from day11 import Day11


# test_data = """0 1 10 99 999"""
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


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day11(data)

#     result = program.solve_part_two()

#     assert result


@pytest.mark.parametrize(
    "line,expected",
    [
        ([125, 17], [253000, 1, 7]),
        (
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
            [
                2097446912,
                14168,
                4048,
                2,
                0,
                2,
                4,
                40,
                48,
                2024,
                40,
                48,
                80,
                96,
                2,
                8,
                6,
                7,
                6,
                0,
                3,
                2,
            ],
        ),
    ],
)
def test_program_function(line, expected):
    result = Day11.blink(line)

    assert result == expected
