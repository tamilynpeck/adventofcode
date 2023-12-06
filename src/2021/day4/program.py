from giant_squid import *

file = "input.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]

numbers, boards = parse_bingo_input(input)

final_score = play_bingo(numbers, boards)
print("winning", final_score)


losing_final_score = play_bingo(numbers, boards, losing=True)
print("losing_final_score", losing_final_score)
