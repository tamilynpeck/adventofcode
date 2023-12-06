from utils import read_file
from day3 import RunsackReorganization

data = read_file("input.txt")

program = RunsackReorganization(data)
result = program.duplicate_item_priority_sum()
print("part 1", result)

result = program.group_badge_item_priority_sum()
print("part 2", result)
