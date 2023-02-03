from aoc2022.day1_calorie_counting import calorie_counting
from aoc2022.day2_rock_paper_scissors import rock_paper_scissors

## DAY 1
PUZZLE_INPUT_FILE = "202201.txt"

result = calorie_counting(PUZZLE_INPUT_FILE)
print("calorie_counting part 1", result)
# 70374

result = calorie_counting(PUZZLE_INPUT_FILE, top=3)
print("calorie_counting part 2", result)
# 204610

## DAY 2
PUZZLE_INPUT_FILE = "202202.txt"
result = rock_paper_scissors(PUZZLE_INPUT_FILE)
print("rock_paper_scissors part 1", result)
# 14069

result = rock_paper_scissors(PUZZLE_INPUT_FILE, guide_type="results")
print("rock_paper_scissors part 2", result)
# 12
