import pytest
from utils import read_txt
from day5 import SupplyStacks, Stacks, CrateMover9000, CrateMover9001

test_data = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_create_stacks():
    data = read_txt(test_data)
    supply_stacks = SupplyStacks(data)

    result = Stacks.create_stacks(supply_stacks.stacks)

    assert result.crate_data == {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }


def test_part_one():
    data = read_txt(test_data)

    supply_stacks = SupplyStacks(data)

    result = supply_stacks.sort_crates(crate_mover=CrateMover9000)

    assert result == "CMZ"


def test_part_two():
    data = read_txt(test_data)

    supply_stacks = SupplyStacks(data)

    result = supply_stacks.sort_crates(crate_mover=CrateMover9001)

    assert result == "MCD"
