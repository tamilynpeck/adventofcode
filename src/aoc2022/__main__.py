from aoc2022.day1_calorie_counting import calorie_counting
from aoc2022.day2_rock_paper_scissors import rock_paper_scissors
from aoc2022.day3_rucksack_reorganization import RunsackReorganization

## DAY 1
PUZZLE_INPUT_FILE = "202201.txt"

result = calorie_counting(PUZZLE_INPUT_FILE)
print("calorie_counting part 1", result)

result = calorie_counting(PUZZLE_INPUT_FILE, top=3)
print("calorie_counting part 2", result)

## DAY 2
PUZZLE_INPUT_FILE = "202202.txt"
result = rock_paper_scissors(PUZZLE_INPUT_FILE)
print("rock_paper_scissors part 1", result)

result = rock_paper_scissors(PUZZLE_INPUT_FILE, guide_type="results")
print("rock_paper_scissors part 2", result)

## DAY 3
rucksack_reorganization = RunsackReorganization()
result = rucksack_reorganization.duplicate_item_priority_sum()
print("rucksack_reorganization part 1", result)

result = rucksack_reorganization.group_badge_item_priority_sum()
print("rucksack_reorganization part 2", result)
