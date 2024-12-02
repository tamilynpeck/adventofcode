from utils import read_file
from day2 import Day2

data = read_file("input.txt")

program = Day2(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)