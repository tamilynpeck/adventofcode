from utils import read_file
from day5 import Almanac

data = read_file("input.txt")

program = Almanac(data)
result = program.get_closest_location()
print("part 1", result)

result = program.get_closest_location_by_seed_pair()
print("part 2", result)
