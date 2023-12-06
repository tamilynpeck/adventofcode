from utils import read_file
from day5 import SupplyStacks, CrateMover9000, CrateMover9001

data = read_file("input.txt")

program = SupplyStacks(data)
result = program.sort_crates(crate_mover=CrateMover9000)
print("part 1", result)

program = SupplyStacks(data)
result = program.sort_crates(crate_mover=CrateMover9001)
print("part 2", result)
