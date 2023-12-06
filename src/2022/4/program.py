from utils import read_file
from day4 import CampCleanup

data = read_file("input.txt")

program = CampCleanup(data)
result = program.find_fully_overlapping()
print("part 1", result)

result = program.find_overlapping()
print("part 2", result)
