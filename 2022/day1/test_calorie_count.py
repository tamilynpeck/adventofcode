file = "test_input.txt"

with open(file) as input_file:
    data = [int(line.strip()) for line in input_file.readlines()]

print(data)
