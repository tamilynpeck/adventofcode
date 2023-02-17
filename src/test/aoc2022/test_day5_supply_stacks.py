from common.FileReader import InMemoryFileReader
from aoc2022.day5_supply_stacks import SupplyStacks, Stacks

file_name = "202205.txt"
test_data = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_create_stacks():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    supply_stacks = SupplyStacks(file_name=file_name, file_reader=file_reader)

    result = Stacks.create_stacks(supply_stacks.stacks)

    assert result.crate_data == {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"],
    }

    # assert result.crate_data == {
    #     1: ["N", "Z"],
    #     2: ["D", "C", "M"],
    #     3: ["P"],
    # }


def test_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    supply_stacks = SupplyStacks(file_name=file_name, file_reader=file_reader)

    result = supply_stacks.sort_crates()

    assert result == "CMZ"
