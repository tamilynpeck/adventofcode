import pytest
from utils import read_txt
from day1 import calorie_counting

test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_elf_with_most_calories():
    data = read_txt(test_data)

    result = calorie_counting(data)

    assert result == 24000


def test_elf_with_most_calories_part_two():
    data = read_txt(test_data)

    result = calorie_counting(data, top=3)

    assert result == 45000
