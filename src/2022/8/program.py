from utils import read_file
from day8 import TreetopTreeHouse

data = read_file("input.txt")

program = TreetopTreeHouse(data)
result = program.visible_trees()
print("part 1", result)

# result = program.part2()
# print("part 2", result)
