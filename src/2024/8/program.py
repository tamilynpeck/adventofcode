from utils import read_file
from day8 import Day8

data = read_file("input.txt")

program = Day8(data)
result = program.solve_part_one()
print("part 1", result)

program = Day8(data)
result = program.solve_part_two()
print("part 2", result)
