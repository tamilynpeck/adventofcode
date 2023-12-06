from utils import read_file
from day4 import Scratchcards

data = read_file("input.txt")

program = Scratchcards(data=data)
result = program.get_card_total()
print("part 1", result)

result = program.get_total_scratchcards()
print("part 2", result)
