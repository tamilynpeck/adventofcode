import pytest
from utils import read_txt
from day11 import Day11

test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_day11():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_one()

    assert result == 374


def test_day11_expand():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.expanded_universe

    expected_data = """..*#.*..*.
..*..*.#*.
#.*..*..*.
**********
..*..*#.*.
.#*..*..*.
..*..*..*#
**********
..*..*.#*.
#.*.#*..*."""
    expected = read_txt(expected_data)

    assert result == expected


def test_day11_part_two():
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_two(exp_distance=2)

    assert result == 374


@pytest.mark.parametrize(
    "exp_distance,expected",
    [
        # (1, ?),
        (2, 374),
        (10, 1030),
        (100, 8410),
    ],
)
def test_program_function(exp_distance, expected):
    data = read_txt(test_data)
    program = Day11(data)

    result = program.solve_part_two(exp_distance=exp_distance)

    assert result == expected


test_map = {
    (1, 2): 5,
    (1, 3): 5,
    (1, 4): 7,
    (1, 5): 7,
    (1, 6): 12,
    (1, 7): 12,
    (1, 8): 12,
    (1, 9): 10,
    (2, 3): 8,
    (2, 4): 5,
    (2, 5): 0,
    (2, 6): 0,
    (2, 7): 0,
    (2, 8): 0,
    (2, 9): 0,
    (3, 4): 0,
    (3, 5): 0,
    (3, 6): 17,
    (3, 7): 0,
    (3, 8): 0,
    (3, 9): 0,
    (4, 5): 0,
    (4, 6): 0,
    (4, 7): 0,
    (4, 8): 0,
    (4, 9): 0,
    (5, 6): 0,
    (5, 7): 0,
    (5, 8): 0,
    (5, 9): 0,
    (6, 7): 0,
    (6, 8): 0,
    (6, 9): 0,
    (7, 8): 0,
    (7, 9): 0,
    (8, 9): 5,
}
