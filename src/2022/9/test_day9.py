import pytest
from utils import read_txt
from day9 import RopeBridge

test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_part_one():
    data = read_txt(test_data)

    rope_bridge = RopeBridge(data)
    result = rope_bridge.simulate_motions()

    assert result == 13
