from common.FileReader import FileReader


class Assignment:
    def __init__(self, range):
        self.range = range
        self.start = self.range[0]
        self.end = self.range[1]

    def contains_value(self, value):
        return self.start <= value <= self.end

    def contains_assignment(self, assignment):
        return self.contains_value(assignment.start) and self.contains_value(
            assignment.end
        )

    def contains_section(self, assignment):
        return self.contains_value(assignment.start) or self.contains_value(
            assignment.end
        )


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def is_overlapping(self):
        return self.first.contains_section(
            self.second
        ) or self.second.contains_section(self.first)

    def is_fully_overlapping(self):
        return self.first.contains_assignment(
            self.second
        ) or self.second.contains_assignment(self.first)


class CampCleanup:
    def __init__(self, file_name="202204.txt", file_reader=FileReader()):
        data = file_reader.read_txt(file_name)
        self.assignments = CampCleanup.parse_data(data)

    def find_fully_overlapping(self):
        overlapping_count = 0
        for first, second in self.assignments:
            pair = Pair(Assignment(first), Assignment(second))
            if pair.is_fully_overlapping():
                overlapping_count += 1

        return overlapping_count

    def find_overlapping(self):
        overlapping_count = 0
        for first, second in self.assignments:
            pair = Pair(Assignment(first), Assignment(second))
            if pair.is_overlapping():
                overlapping_count += 1

        return overlapping_count

    @staticmethod
    def parse_data(data):
        parse_range = lambda x: [int(x) for x in x.split("-")]
        return [[parse_range(range) for range in row.split(",")] for row in data]
