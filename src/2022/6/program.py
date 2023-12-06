from utils import read_file
from day6 import TuningTrouble

data = read_file("input.txt")

program = TuningTrouble(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)
