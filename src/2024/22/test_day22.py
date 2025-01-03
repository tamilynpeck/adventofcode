import pytest
from utils import read_txt
from day22 import Day22


test_data = """1
10
100
2024"""


def test_part_one():
    data = read_txt(test_data)
    program = Day22(data)

    result = program.solve_part_one()

    assert result == 37327623


def test_part_two():
    test_data = """1
2
3
2024"""
    data = read_txt(test_data)
    program = Day22(data)

    result = program.solve_part_two()

    assert result == 23


@pytest.mark.parametrize(
    "line,expected",
    [
        (123, 15887950),
        (15887950, 16495136),
        (16495136, 527345),
        (527345, 704524),
        (704524, 1553684),
        (1553684, 12683156),
        (12683156, 11100544),
        (11100544, 12249484),
        (12249484, 7753432),
        (7753432, 5908254),
    ],
)
def test_next_number(line, expected):
    data = read_txt(test_data)
    program = Day22(data)

    result = program.next_number(line)

    assert result == expected


def test_next_number_123():
    data = read_txt(test_data)
    program = Day22(data)

    number = 123
    for _ in range(10):
        number = program.next_number(number)

    assert number == 5908254


@pytest.mark.parametrize(
    "number,expected",
    [(1, 8685429), (10, 4700978), (100, 15273692), (2024, 8667524)],
)
def test_next_number_2000(number, expected):
    data = read_txt(test_data)
    program = Day22(data)

    number = program.get_secret_number_n(number)

    assert number == expected


def test_logic():
    # (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    result = 100000000 % 16777216
    assert result == 16113920

    # If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    result = 42 ^ 15
    assert result == 37

    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    result = 60 // 32
    assert result == 1


@pytest.mark.parametrize(
    "number,expected",
    [(1, 7), (2, 7), (3, None), (2024, 9)],
)
def test_next_number_2000(number, expected):
    data = read_txt(test_data)
    program = Day22(data)

    number = program.get_secret_number_pattern(number)

    assert number == expected
