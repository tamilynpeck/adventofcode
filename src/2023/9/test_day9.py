import pytest
from utils import read_txt
from day9 import Day9

test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_day9():
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_one()

    assert result == 114


def test_day9_negatives():
    test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7"""

    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_one()

    assert result == 114 + (-8)


def test_day9_part_two():
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_two()

    assert result == 2


@pytest.mark.parametrize(
    "history,expected",
    [
        ([0, 3, 6, 9, 12, 15], 18),
        ([1, 3, 6, 10, 15, 21], 28),
        ([10, 13, 16, 21, 30, 45], 68),
        (
            [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7],
            -8,
        ),
        (
            [
                1,
                -1,
                -3,
                -5,
                -7,
                -9,
                -11,
                -13,
                -15,
                -17,
                -19,
                -21,
                -23,
                -25,
                -27,
                -29,
                -31,
                -33,
                -35,
                -37,
                -39,
            ],
            -41,
        ),
        (
            [
                17,
                20,
                19,
                14,
                5,
                -8,
                -25,
                -46,
                -71,
                -100,
                -133,
                -170,
                -211,
                -256,
                -305,
                -358,
                -415,
                -476,
                -541,
                -610,
                -683,
            ],
            -760,
        ),
    ],
)
def test_program_function(history, expected):
    result = Day9.solve_next_in_history(history)

    assert result == expected
