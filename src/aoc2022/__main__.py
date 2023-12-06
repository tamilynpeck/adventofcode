from aoc2022.day1_calorie_counting import calorie_counting


PUZZLE_INPUT_FILE = "202201.txt"
result = calorie_counting(PUZZLE_INPUT_FILE)
print("calorie_counting part 1", result)

result = calorie_counting(PUZZLE_INPUT_FILE, top=3)
print("calorie_counting part 2", result)
