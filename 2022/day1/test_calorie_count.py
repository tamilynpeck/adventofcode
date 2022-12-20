from calorie_counting import calorie_counting


def test_elf_with_most_calories():
    file = "test_input.txt"

    result = calorie_counting(file)
    assert result == 24000


def test_real_input():
    puzzle_input_file = "input.txt"
    result = calorie_counting(puzzle_input_file)

    print("result", result)
    assert result == 71471


def test_real_input_part_two():
    puzzle_input_file = "input.txt"
    result = calorie_counting(puzzle_input_file, top=3)

    print("result", result)
    assert result == 211189


def test_real_input_b():
    puzzle_input_file = "input_b.txt"
    result = calorie_counting(puzzle_input_file)

    print("result", result)
    assert result == 70374

def test_real_input_part_two_b():
    puzzle_input_file = "input_b.txt"
    result = calorie_counting(puzzle_input_file, top=3)

    print("result", result)
    assert result == 204610