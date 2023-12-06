import pytest
from utils import read_txt
from day6 import TuningTrouble

test_data = ""


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
    data = read_txt(test_data)

    tuning_trouble = TuningTrouble(data)

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
    data = read_txt(test_data)

    tuning_trouble = TuningTrouble(data)

    result = tuning_trouble.solve_part_two()

    assert result == expected_result
