import pytest
from utils import read_txt
from day2 import rock_paper_scissors

test_data = """A Y
B X
C Z"""


def test_rock_paper_scissors_part_one():
    data = read_txt(test_data)

    result = rock_paper_scissors(data)

    assert result == 15


def test_rock_paper_scissors_part_two():
    data = read_txt(test_data)

    result = rock_paper_scissors(
        data,
        guide_type="results",
    )

    assert result == 12
