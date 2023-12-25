import pytest
from utils import read_txt
from day24 import Day24, line_intersection

test_data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def test_day24():
    data = read_txt(test_data)
    program = Day24(data, min=7, max=27)

    result = program.solve_part_one()

    assert result == 2


@pytest.mark.parametrize(
    "data,expected",
    [
        (
            ["19, 13, 30 @ -2,  1, -2", "18, 19, 22 @ -1, -1, -2"],
            (14.333333333333334, 15.333333333333334),
        ),
    ],
)
def test_program_function(data, expected):
    program = Day24(data)
    line1 = program.data[0]
    lines2 = program.data[1]

    result = line_intersection(line1, lines2)

    assert result == expected
