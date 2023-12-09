import pytest
from utils import read_txt
from day8 import Day8


def test_day8():
    test_data = """RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)"""

    data = read_txt(test_data)
    program = Day8(data)

    result = program.solve_part_one()

    assert result == 2


def test_day8_second():
    test_data = """LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)"""

    data = read_txt(test_data)
    program = Day8(data)

    result = program.solve_part_one()

    assert result == 6


def test_day8_part_two():
    test_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    data = read_txt(test_data)
    program = Day8(data)

    result = program.solve_part_two()

    assert result == 6
