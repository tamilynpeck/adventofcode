from common.FileReader import InMemoryFileReader
from aoc2022.day7_no_space_left_on_device import SpaceAnalyzer

file_name = "202207.txt"
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
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)
    space_analyzer = SpaceAnalyzer(file_name=file_name, file_reader=file_reader)

    directories = space_analyzer.group_directories()

    assert directories["/"] == 48381165
    assert directories["/-a"] == 94853
    assert directories["/-d"] == 24933642
    assert directories["/-a-e"] == 584


def test_part_one_solution():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)
    space_analyzer = SpaceAnalyzer(file_name=file_name, file_reader=file_reader)

    result = space_analyzer.solve_part_one()

    assert result == 95437

def test_part_two_solution():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)
    space_analyzer = SpaceAnalyzer(file_name=file_name, file_reader=file_reader)

    result = space_analyzer.solve_part_two()

    assert result == 24933642
