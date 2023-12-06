from functools import reduce


class Day6:
    def __init__(self, data):
        self.time = data[0].split(":")[1].strip()
        self.record_distance = data[1].split(":")[1].strip()

    def solve_part_one(self):
        time = (
            self.time.replace("   ", " ")
            .replace("  ", " ")
            .replace("  ", " ")
            .split(" ")
        )
        record_distance = (
            self.record_distance.replace("   ", " ").replace("  ", " ").split(" ")
        )

        return self.calculate_options(time, record_distance)

    def solve_part_two(self):
        time = self.time.replace(" ", "").split(" ")
        record_distance = self.record_distance.replace(" ", "").split(" ")
        return self.calculate_options(time, record_distance)

    def calculate_options(self, time, record_distance):
        count_options = []
        for i in range(len(time)):
            options = Day6.button_math(int(time[i]), int(record_distance[i]))
            count_options.append(options)

        return reduce(lambda x, y: x * y, count_options)

    def button_math(time, record_distance):
        options = []
        for i in range(time):
            hold_time = i + 1
            time_remaining = time - hold_time
            distance = hold_time * time_remaining
            if distance > record_distance:
                options.append(distance)

        return len(options)
