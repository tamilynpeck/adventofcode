import pytest
from utils import read_txt
from day3 import GearRatios


def test_gear_ratios():
    test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    data = read_txt(test_data)
    gear = GearRatios(data)

    result = gear.get_gear_part_total()

    assert result == 4361


def test_gear_ratios_2():
    test_data = """467..114..
...*......
..35..633.
./....#.*1
617%......
.....+.58.
.$592.755.
..........
...$.*....
.664.598.."""

    data = read_txt(test_data)
    gear = GearRatios(data)

    result = gear.get_gear_part_total()

    assert result == 4362


def test_searching():
    test_data = """467..114.."""
    data = read_txt(test_data)
    gear = GearRatios(data)

    result = gear.search_for_symbol(0, 1)

    assert result == False


def test_gear_ratios():
    test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    data = read_txt(test_data)
    gear = GearRatios(data)

    result = gear.get_gear_ratios()

    assert result == 467835


def test_gear_ratios_multiple_on_one_row():
    test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
..598.755.
...$.*....
.664......"""

    data = read_txt(test_data)
    gear = GearRatios(data)

    result = gear.get_gear_ratios()

    assert result == 467835
