from utils import read_file
from day7 import SpaceAnalyzer

data = read_file("input.txt")

program = SpaceAnalyzer(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)
