from aoc2022.calorie_counting import calorie_counting

## DAY 1
# 71471
# 211189
PUZZLE_INPUT_FILE = "day_1_input.txt"
result = calorie_counting(PUZZLE_INPUT_FILE)
print("calorie_counting part 1", result)

result = calorie_counting(PUZZLE_INPUT_FILE, top=3)
print("calorie_counting part 2", result)

