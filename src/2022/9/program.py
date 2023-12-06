from utils import read_file
from day9 import RopeBridge

data = read_file("input.txt")

program = RopeBridge(data)
result = program.simulate_motions()
print("part 1", result)

# result = program.part2()
# print("part 2", result)
