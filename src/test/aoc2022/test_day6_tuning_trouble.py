import pytest
from common.FileReader import InMemoryFileReader
from aoc2022.day6_tuning_trouble import TuningTrouble

test_name = "202206.txt"


@pytest.mark.parametrize(
    "test_data,expected_result",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part_one(test_data, expected_result):
    file_reader = InMemoryFileReader()
    file_reader.setup(test_name, test_data)

    tuning_trouble = TuningTrouble(file_name=test_name, file_reader=file_reader)

    result = tuning_trouble.solve_part_one()

    assert result == expected_result


@pytest.mark.parametrize(
    "test_data,expected_result",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_part_two(test_data, expected_result):
    file_reader = InMemoryFileReader()
    file_reader.setup(test_name, test_data)

    tuning_trouble = TuningTrouble(file_name=test_name, file_reader=file_reader)

    result = tuning_trouble.solve_part_two()

    assert result == expected_result
