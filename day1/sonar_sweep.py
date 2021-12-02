# How many measurements are larger than the previous measurement?

file = "input.txt"

with open(file) as input_file:
    depths = [int(line.strip()) for line in input_file.readlines()]


def count_increases(numbers):
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            count += 1
    return count


increase_count = count_increases(depths)

print(len(depths))
print(increase_count)
print(depths[-3:])


combined_depths = []

for d in range(2, len(depths)):
    combined_depths.append(sum(depths[d - 2:d + 1]))

increase_count = count_increases(combined_depths)

print(len(combined_depths))
print(increase_count)

print("first", sum([119,121,129]))
print(combined_depths[:1])
print("last", sum([6210,6212,6217]))
print(combined_depths[-3:])


