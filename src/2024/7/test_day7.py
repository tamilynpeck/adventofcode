import pytest
from utils import read_txt
from day7 import Day7


test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_part_one():
    data = read_txt(test_data)
    program = Day7(data)

    result = program.solve_part_one()

    assert result == 3749


def test_part_two():
    data = read_txt(test_data)
    program = Day7(data)

    result = program.solve_part_two()

    assert result == 11387


@pytest.mark.parametrize(
    "value, numbers, expected",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
        (83, [17, 5], False),
        (156, [15, 6], False),
        (7290, [6, 8, 6, 15], False),
        (161011, [16, 10, 13], False),
        (192, [17, 8, 14], False),
        (21037, [9, 7, 18, 13], False),
        (292, [11, 6, 16, 20], True),
    ],
)
def test_program_function(value, numbers, expected):
    program = Day7([])

    result = program.test_combinations(value, numbers)

    assert result == expected


@pytest.mark.parametrize(
    "value, numbers, expected",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
        (83, [17, 5], False),
        (156, [15, 6], True),
        (7290, [6, 8, 6, 15], True),
        (161011, [16, 10, 13], False),
        (192, [17, 8, 14], True),
        (21037, [9, 7, 18, 13], False),
        (292, [11, 6, 16, 20], True),
    ],
)
def test_program_function_part_two(value, numbers, expected):
    program = Day7([])

    result = program.test_combinations(value, numbers, True)

    assert result == expected
