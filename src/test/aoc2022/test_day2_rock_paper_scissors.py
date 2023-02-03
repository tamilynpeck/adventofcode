from aoc2022.day2_rock_paper_scissors import rock_paper_scissors
from common.FileReader import InMemoryFileReader

TEST_INPUT_FILE = "year2022_day2_test.txt"

test_data = """A Y
B X
C Z"""


def test_memory_reader():
    file_reader = InMemoryFileReader()
    file_reader.setup(TEST_INPUT_FILE, test_data)

    result = file_reader.read_txt(TEST_INPUT_FILE)

    assert result == ["A Y", "B X", "C Z"]


def test_rock_paper_scissors_part_one():
    file_reader = InMemoryFileReader()
    file_reader.setup(TEST_INPUT_FILE, test_data)

    result = rock_paper_scissors(TEST_INPUT_FILE, file_reader=file_reader)

    assert result == 15


def test_rock_paper_scissors_part_two():
    file_reader = InMemoryFileReader()
    file_reader.setup(TEST_INPUT_FILE, test_data)

    result = rock_paper_scissors(
        TEST_INPUT_FILE, guide_type="results", file_reader=file_reader
    )

    assert result == 12
