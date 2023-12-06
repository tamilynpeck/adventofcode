from utils import read_file
from day3 import GearRatios

data = read_file("input.txt")

program = GearRatios(data=data)
result = program.get_gear_part_total()
print("part 1", result)

result = program.get_gear_ratios()
print("part 2", result)
