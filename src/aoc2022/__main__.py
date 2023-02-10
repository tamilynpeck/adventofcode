from aoc2022.day1_calorie_counting import calorie_counting
from aoc2022.day2_rock_paper_scissors import rock_paper_scissors

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

from aoc2022.day3_rucksack_reorganization import RunsackReorganization

result = RunsackReorganization().duplicate_item_priority_sum()
print("rucksack_reorganization part 1", result)

result = RunsackReorganization().group_badge_item_priority_sum()
print("rucksack_reorganization part 2", result)

from aoc2022.day4_camp_cleanup import CampCleanup

result = CampCleanup().find_fully_overlapping()
print("camp_cleanup part 1", result)

result = CampCleanup().find_overlapping()
print("camp_cleanup part 2", result)
