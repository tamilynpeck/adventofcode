from LanternFish import LanternFish

file = "input.txt"

with open(file) as input_file:
    numbers = [line.strip() for line in input_file.readlines()]
    input = [int(n) for n in numbers[0].split(",")]


fish = LanternFish(input)


print(input)
fish_count = fish.days(80)
print(fish_count)

fish_count = fish.days(256)
print(fish_count)
