from utils import read_file
from day19 import Day19

data = read_file("input.txt")

program = Day19(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)