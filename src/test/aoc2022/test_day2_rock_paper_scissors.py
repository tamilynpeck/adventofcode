from aoc2022.day2_rock_paper_scissors import rock_paper_scissors
from common.FileReader import InMemoryFileReader

file_name = "year2022_day2_test.txt"

test_data = """A Y
B X
C Z"""


def test_rock_paper_scissors_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    result = rock_paper_scissors(file_name, file_reader=file_reader)

    assert result == 15


def test_rock_paper_scissors_part_two():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, test_data)

    result = rock_paper_scissors(
        file_name, guide_type="results", file_reader=file_reader
    )

    assert result == 12
