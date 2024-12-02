class Day2:
    def __init__(self, data):
        self.data = [list(map(int, line.split())) for line in data]

    def solve_part_one(self):
        return sum([is_safe(report) for report in self.data])

    def solve_part_two(self):
        return sum([is_safe_dampener(report) for report in self.data])


def is_safe(report):
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    # if not all positive or not all negative, not safe
    if not all(d > 0 for d in diffs) and not all(d < 0 for d in diffs):
        return False
    # if abs diff is between 1 and 3, safe
    if all(abs(d) in [1, 2, 3] for d in diffs):
        return True
    return False


def is_safe_dampener(report):
    if is_safe(report):
        return True
    # remove one element at a time and check if safe
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False
