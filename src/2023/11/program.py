from utils import read_file
from day11 import Day11

data = read_file("input.txt")

program = Day11(data)
result = program.solve_part_one()
print("part 1", result)
assert result == 10077850

result = program.solve_part_two(exp_distance=1000000)
print("part 2", result)
assert result == 504715068438
