import pytest
from utils import read_txt
from day9 import Day9


test_data = """2333133121414131402"""


def test_part_one():
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_one()

    assert result == 1928


def test_part_two():
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_two()

    assert result == 2858


def test_part_two_test_case_1():
    test_data = """1313165"""
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_two()

    assert result == 169


def test_part_two_test_case_2():
    test_data = """9953877292941"""
    data = read_txt(test_data)
    program = Day9(data)

    result = program.solve_part_two()

    assert result == 5768


@pytest.mark.parametrize(
    "line,expected",
    [
        ([1, 2, 3, 4, 5], [0, ".", ".", 1, 1, 1, ".", ".", ".", ".", 2, 2, 2, 2, 2]),
        (
            [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2],
            [
                0,
                0,
                ".",
                ".",
                ".",
                1,
                1,
                1,
                ".",
                ".",
                ".",
                2,
                ".",
                ".",
                ".",
                3,
                3,
                3,
                ".",
                4,
                4,
                ".",
                5,
                5,
                5,
                5,
                ".",
                6,
                6,
                6,
                6,
                ".",
                7,
                7,
                7,
                ".",
                8,
                8,
                8,
                8,
                9,
                9,
            ],
        ),
    ],
)
def test_individual_blocks(line, expected):
    program = Day9("123")

    result = program.individual_blocks(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            [
                0,
                0,
                ".",
                ".",
                ".",
                1,
                1,
                1,
                ".",
                ".",
                ".",
                2,
                ".",
                ".",
                ".",
                3,
                3,
                3,
                ".",
                4,
                4,
                ".",
                5,
                5,
                5,
                5,
                ".",
                6,
                6,
                6,
                6,
                ".",
                7,
                7,
                7,
                ".",
                8,
                8,
                8,
                8,
                9,
                9,
            ],
            [
                0,
                0,
                9,
                9,
                8,
                1,
                1,
                1,
                8,
                8,
                8,
                2,
                7,
                7,
                7,
                3,
                3,
                3,
                6,
                4,
                4,
                6,
                5,
                5,
                5,
                5,
                6,
                6,
            ],
        ),
        (
            [0, ".", ".", 1, 1, 1, ".", ".", ".", ".", 2, 2, 2, 2, 2],
            [0, 2, 2, 1, 1, 1, 2, 2, 2],
        ),
    ],
)
def test_free_disk_space(line, expected):
    program = Day9("123")

    result = program.file_compacting(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            [
                0,
                0,
                9,
                9,
                8,
                1,
                1,
                1,
                8,
                8,
                8,
                2,
                7,
                7,
                7,
                3,
                3,
                3,
                6,
                4,
                4,
                6,
                5,
                5,
                5,
                5,
                6,
                6,
            ],
            1928,
        ),
        (
            [
                0,
                0,
                9,
                9,
                2,
                1,
                1,
                1,
                7,
                7,
                7,
                ".",
                4,
                4,
                ".",
                3,
                3,
                3,
                ".",
                ".",
                ".",
                ".",
                5,
                5,
                5,
                5,
                ".",
                6,
                6,
                6,
                6,
                ".",
                ".",
                ".",
                ".",
                ".",
                8,
                8,
                8,
                8,
                ".",
                ".",
            ],
            2858,
        ),
        (
            [
                0,
                0,
                9,
                9,
                ".",
            ],
            45,
        ),
    ],
)
def test_checksum(line, expected):
    program = Day9("123")

    result = program.checksum(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            [
                [
                    0,
                    0,
                ],
                [".", ".", "."],
                [
                    1,
                    1,
                    1,
                ],
                [".", ".", "."],
                [2],
                [".", ".", "."],
                [3, 3, 3],
                ["."],
                [4, 4],
                ["."],
                [5, 5, 5, 5],
                ["."],
                [6, 6, 6, 6],
                ["."],
                [
                    7,
                    7,
                    7,
                ],
                ["."],
                [8, 8, 8, 8],
                [9, 9],
            ],
            [
                [
                    0,
                    0,
                ],
                [9, 9],
                [2],
                [1, 1, 1],
                [7, 7, 7],
                ["."],
                [4, 4],
                ["."],
                [
                    3,
                    3,
                    3,
                ],
                [".", ".", ".", "."],
                [
                    5,
                    5,
                    5,
                    5,
                ],
                ["."],
                [6, 6, 6, 6],
                [".", ".", ".", ".", "."],
                [8, 8, 8, 8],
                [".", "."],
            ],
        ),
        (
            [
                [0],
                [".", "."],
                [
                    1,
                    1,
                    1,
                ],
                [".", ".", ".", "."],
                [2, 2, 2, 2, 2],
            ],
            [
                [0],
                [".", "."],
                [
                    1,
                    1,
                    1,
                ],
                [".", ".", ".", "."],
                [2, 2, 2, 2, 2],
            ],
        ),
        (
            [[0, 0], [".", ".", ".", "."], [11, 11]],
            [[0, 0], [11, 11], [".", ".", ".", "."]],
        ),
        (
            [[0, 0], [".", ".", ".", "."], [11, 11, 11]],
            [[0, 0], [".", ".", ".", "."], [11, 11, 11]],
        ),
        (
            [[0, 0], [".", ".", ".", "."], [113]],
            [[0, 0], [113], [".", ".", ".", "."]],
        ),
    ],
)
def test_file_compacting_part_two(line, expected):
    program = Day9("123")

    result = program.file_compacting_part_two(line)

    assert result == expected


@pytest.mark.parametrize(
    "numbers,expected",
    [
        (
            [1, 2, 3, 4, 5],
            [
                [0],
                [".", "."],
                [
                    1,
                    1,
                    1,
                ],
                [".", ".", ".", "."],
                [2, 2, 2, 2, 2],
            ],
        ),
    ],
)
def test_individual_blocks_part_two(numbers, expected):
    program = Day9("123")

    result = program.individual_blocks_part_two(numbers)

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            [
                [0, 0],
                [9, 9],
                [2],
                [1, 1, 1],
                [7, 7, 7],
                ["."],
                [4, 4],
                ["."],
                [3, 3, 3],
                [".", ".", ".", "."],
                [5, 5, 5, 5],
                ["."],
                [6, 6, 6, 6],
                [".", ".", ".", ".", "."],
                [8, 8, 8, 8],
                [],
                [".", "."],
            ],
            2858,
        ),
    ],
)
def test_checksum_part_two(line, expected):
    program = Day9("123")

    result = program.checksum_part_two(line)

    assert result == expected
