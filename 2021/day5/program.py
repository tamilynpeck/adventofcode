from HydrothermalVenture import HydrothermalVenture

file = "input.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]


venture = HydrothermalVenture(input)

print(venture.overlap_points)


venture_diagonal = HydrothermalVenture(input, diagonal=True)

print("diagonal", venture_diagonal.overlap_points)