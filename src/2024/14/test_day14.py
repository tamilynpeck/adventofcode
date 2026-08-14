import pytest
from utils import read_txt
from day14 import Day14, Robot


test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

max_x = 11
max_y = 7


def test_part_one():
    data = read_txt(test_data)
    program = Day14(data)

    result = program.solve_part_one(max_x=11, max_y=7)

    positions = [r.position for r in program.robots]
    print(positions)

    assert (0, 2) in positions
    assert (6, 0) in positions
    assert (9, 0) in positions

    assert result == 12


# def test_part_two():
#     data = read_txt(test_data)
#     program = Day14(data)

#     result = program.solve_part_two()

#     assert result == 0


@pytest.mark.parametrize(
    "position,velocity,expected",
    [
        ((6, 3), (-1, -3), (5, 0)),
        ((10, 3), (-1, 2), (9, 5)),
        ((2, 0), (2, -1), (4, 6)),
        ((0, 0), (1, 3), (1, 3)),
        ((3, 0), (-2, -2), (1, 5)),
        ((7, 6), (-1, -3), (6, 3)),
        ((3, 0), (-1, -2), (2, 5)),
        ((9, 3), (2, 3), (0, 6)),
        ((7, 3), (-1, 2), (6, 5)),
        ((9, 5), (-3, -3), (6, 2)),
        ##
        ((2, 4), (2, -3), (4, 1)),
        ((4, 1), (2, -3), (6, 5)),
        ((6, 5), (2, -3), (8, 2)),
        ((8, 2), (2, -3), (10, 6)),
        ((10, 6), (2, -3), (1, 3)),
    ],
)
def test_program_function(position, velocity, expected):
    robot = Robot(position, velocity)

    robot.teleport(max_x, max_y)

    assert robot.position == expected


def test_seconds():
    robot = Robot((2, 4), (2, -3))

    for i in range(0, 5):
        robot.teleport(max_x, max_y)

    assert robot.position == (1, 3)
