import pytest
from common.FileReader import MemoryDataReader
from aoc2023.day2_cube_conundrum import CubeConundrum

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def test_cube_conundrum():
    reader = MemoryDataReader(test_data)
    cube = CubeConundrum(reader.data)

    result = cube.possible_games(red=12, green=13, blue=14)

    assert result == 8

@pytest.mark.parametrize(
    "line,expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ],
)
def test_cube_conundrum_power(line, expected):
    reader = MemoryDataReader(line)
    cube = CubeConundrum(reader.data)

    result = cube.power()

    assert result == expected

def test_cube_conundrum_power_total():
    reader = MemoryDataReader(test_data)
    cube = CubeConundrum(reader.data)

    result = cube.power()

    assert result == 2286

