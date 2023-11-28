from common.FileReader import InMemoryFileReader
from aoc2022.day8_treetop_tree_house import TreetopTreeHouse

file_name = "202208.txt"
test_data = """30373
25512
65332
33549
35390"""


def test_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    treetop_tree_house = TreetopTreeHouse(file_reader=file_reader)
    result = treetop_tree_house.visible_trees()

    assert result == 21
