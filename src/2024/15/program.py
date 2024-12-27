from utils import read_file
from day15 import Day15
from day15_part2 import Day15Part2

data = read_file("input.txt")

program = Day15(data)
result = program.solve_part_one()
print("part 1", result)

program = Day15Part2(data)
result = program.solve_part_two()
print("part 2", result)
