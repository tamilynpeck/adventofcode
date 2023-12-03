import pytest
from common.FileReader import MemoryDataReader
from aoc2023.day3_gear_ratios import GearRatios


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

    reader = MemoryDataReader(test_data)
    gear = GearRatios(reader.data)

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

    reader = MemoryDataReader(test_data)
    gear = GearRatios(reader.data)

    result = gear.get_gear_part_total()

    assert result == 4362


def test_searching():
    test_data = """467..114.."""
    reader = MemoryDataReader(test_data)
    gear = GearRatios(reader.data)

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

    reader = MemoryDataReader(test_data)
    gear = GearRatios(reader.data)

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

    reader = MemoryDataReader(test_data)
    gear = GearRatios(reader.data)

    result = gear.get_gear_ratios()

    assert result == 467835
