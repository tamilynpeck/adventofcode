from utils import read_file
from day4 import Day4

data = read_file("input.txt")

program = Day4(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)