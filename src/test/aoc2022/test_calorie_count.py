from aoc2022.calorie_counting import calorie_counting


def test_elf_with_most_calories():
    file = "year2022_day1_test.txt"

    result = calorie_counting(file)
    assert result == 24000
