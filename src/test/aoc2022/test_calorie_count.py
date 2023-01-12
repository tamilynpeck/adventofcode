from aoc2022.calorie_counting import calorie_counting


def test_elf_with_most_calories():
    file = "day1_test_input.txt"

    result = calorie_counting(file)
    assert result == 24000
