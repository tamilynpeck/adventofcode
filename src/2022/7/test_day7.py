import pytest
from utils import read_txt
from day7 import SpaceAnalyzer

test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_part_one_group_directories():
    data = read_txt(test_data)
    space_analyzer = SpaceAnalyzer(data)

    directories = space_analyzer.group_directories()

    assert directories["/"] == 48381165
    assert directories["/-a"] == 94853
    assert directories["/-d"] == 24933642
    assert directories["/-a-e"] == 584


def test_part_one_solution():
    data = read_txt(test_data)
    space_analyzer = SpaceAnalyzer(data)

    result = space_analyzer.solve_part_one()

    assert result == 95437


def test_part_two_solution():
    data = read_txt(test_data)
    space_analyzer = SpaceAnalyzer(data)

    result = space_analyzer.solve_part_two()

    assert result == 24933642
