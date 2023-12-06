from utils import read_file
from day2 import rock_paper_scissors

data = read_file("input.txt")


result = rock_paper_scissors(data)
print("part 1", result)

result = rock_paper_scissors(data, guide_type="results")
print("part 2", result)
