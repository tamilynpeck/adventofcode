import pytest
from utils import read_txt
from day12 import Day12

test_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_day12():
    data = read_txt(test_data)
    program = Day12(data)

    # result = program.solve_part_one()

    # assert result == 21


@pytest.mark.parametrize(
    "line,expected",
    [
        ("???.### 1,1,3", 1),
        # (".??..??...?##. 1,1,3", 4),
        # ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        # ("????.######..#####. 1,6,5", 4),
        # ("?###???????? 3,2,1", 10),
    ],
)
def test_arrangement(line, expected):
    data = read_txt(line)
    program = Day12(data)

    result = program.possible_arrangements(line)

    assert result == expected


@pytest.mark.parametrize(
    "line,groups,expected",
    [
        ("####.#...#...", [4, 1, 1], True),
        ("????.######..#####.", [1, 6, 5], False),
    ],
)
def test_match(line, groups, expected):
    data = read_txt(line)
    program = Day12(data)

    result = program.is_match(line, groups)

    assert result == expected
