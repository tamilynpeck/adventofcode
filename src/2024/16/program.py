from utils import read_file
from day16 import Day16

data = read_file("input.txt")

program = Day16(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)