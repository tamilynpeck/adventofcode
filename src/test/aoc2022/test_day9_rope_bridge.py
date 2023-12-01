from common.FileReader import MemoryDataReader
from aoc2022.day9_rope_bridge import RopeBridge

test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_part_one():
    reader = MemoryDataReader(test_data)

    rope_bridge = RopeBridge(data=reader.data)
    result = rope_bridge.simulate_motions()

    assert result == 13
