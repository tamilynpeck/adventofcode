from Whales import Whales

file = "input.txt"

with open(file) as input_file:
    numbers = [line.strip() for line in input_file.readlines()]
    input = [int(n) for n in numbers[0].split(",")]


whales = Whales(input)

print(whales.lowest_fuel())

print(whales.lowest_fuel(exponential_cost=True))
