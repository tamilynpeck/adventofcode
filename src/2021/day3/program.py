from binary_diagnostic import BinaryDiagnostic

file = "input.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]

diagnostic = BinaryDiagnostic(input)

diagnostic.calculate()

print(diagnostic.gamma)
print(diagnostic.epsilon)
print(diagnostic.power_consumption)

print(diagnostic.oxygen_generator_rating)
print(diagnostic.c02_scrubber)
print(diagnostic.life_support_rating)