import pytest
from utils import read_txt
from day2 import Day2


test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def test_part_one():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_one()

    assert result == 1227775554


def test_part_two():
    data = read_txt(test_data)
    program = Day2(data)

    result = program.solve_part_two()

    assert result == 4174379265


@pytest.mark.parametrize(
    "id_range,expected",
    [
        ("11-22", [11, 22]),
        ("95-115", [99]),
        ("998-1012", [1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", []),
        ("824824821-824824827", []),
        ("2121212118-2121212124", []),
    ],
)
def test_program_function(id_range, expected):
    program = Day2(test_data)

    result = program.invalid_id(id_range)

    assert result == expected


@pytest.mark.parametrize(
    "id_range,expected",
    [
        ("11-22", [11, 22]),
        ("95-115", [99, 111]),
        ("998-1012", [999, 1010]),
        ("1188511880-1188511890", [1188511885]),
        ("222220-222224", [222222]),
        ("1698522-1698528", []),
        ("446443-446449", [446446]),
        ("38593856-38593862", [38593859]),
        ("565653-565659", [565656]),
        ("824824821-824824827", [824824824]),
        ("2121212118-2121212124", [2121212121]),
    ],
)
def test_program_function_part_two(id_range, expected):
    program = Day2(test_data)

    result = program.invalid_id_part_two(id_range)

    assert result == expected
