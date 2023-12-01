from common.FileReader import InMemoryFileReader
from aoc2022.day9_rope_bridge import RopeBridge

file_name = "202209.txt"
test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    rope_bridge = RopeBridge(file_reader=file_reader)
    result = rope_bridge.solve_part_one()

    assert result == 13
