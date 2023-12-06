import pytest
from utils import read_txt
from day8 import TreetopTreeHouse

test_data = """30373
25512
65332
33549
35390"""


def test_part_one():
    data = read_txt(test_data)

    treetop_tree_house = TreetopTreeHouse(data)
    result = treetop_tree_house.visible_trees()

    assert result == 21
