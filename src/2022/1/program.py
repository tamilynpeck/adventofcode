from utils import read_file
from day1 import calorie_counting

data = read_file("input.txt")

result = calorie_counting(data)
print("part 1", result)

result = calorie_counting(data, top=3)
print("part 2", result)
