from calorie_counting import calorie_counting


def test_elf_with_most_calories():
    file = "test_input.txt"

    result = calorie_counting(file)
    assert result == 24000


def test_real_input():
    PUZZLE_INPUT_FILE = "input.txt"
    result = calorie_counting(PUZZLE_INPUT_FILE)

    print("result", result)
    assert result == 71471


def test_real_input_part_two():
    PUZZLE_INPUT_FILE = "input.txt"
    result = calorie_counting(PUZZLE_INPUT_FILE, top=3)

    print("result", result)
    assert result == 211189
