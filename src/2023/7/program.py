from utils import read_file
from day7 import Day7

data = read_file("input.txt")

program = Day7(data)
result = program.solve_part_one()
print("part 1", result)

program = Day7(data, wild=True)
result = program.solve_part_two()
print("part 2", result)
# too low 209893404
# too low 217869386
# too low 251293241
# 251528448
# 251528448
# 251528448
