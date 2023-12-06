from utils import read_file
from day2 import CubeConundrum

data = read_file("input.txt")

program = CubeConundrum(data=data)
result = program.possible_games(red=12, green=13, blue=14)
print("part 1", result)

result = program.power()
print("part 2", result)
