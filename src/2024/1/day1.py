class Day1:
    def __init__(self, data):
        self.data = data
        self.left_list = []
        self.right_list = []
        for line in data:
            left, right = line.split()
            self.left_list.append(int(left))
            self.right_list.append(int(right))

    def solve_part_one(self):
        self.left_list.sort()
        self.right_list.sort()

        total_distance = 0

        for i in range(len(self.left_list)):
            total_distance += abs(self.left_list[i] - self.right_list[i])

        return total_distance

    def solve_part_two(self):
        # Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
        return sum([value * self.right_list.count(value) for value in self.left_list])
