from utils import read_file
from day1 import Trebuchet

data = read_file("input.txt")

trebuchet = Trebuchet(data=data)
result = trebuchet.calibrate_sum()
print("part 1", result)

result = trebuchet.calibrate_sum_after_interpreting_data()
print("part 2", result)
