import pytest
from utils import read_txt
from day15 import Day15, hash_algorithm

test_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_day15():
    data = read_txt(test_data)
    program = Day15(data)

    result = program.solve_part_one()

    assert result == 1320


def test_day15_part_two():
    data = read_txt(test_data)
    program = Day15(data)

    result = program.solve_part_two()

    assert result == 145


@pytest.mark.parametrize(
    "step,expected",
    [
        ("rn", 0),
        ("cm", 0),
        ("qp", 1),
        ("pc", 3),
        ("ot", 3),
        ("ab", 3),
    ],
)
def test_program_function(step, expected):
    result = hash_algorithm(step)

    assert result == expected
