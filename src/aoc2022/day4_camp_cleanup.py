from common.FileReader import FileReader


class CampCleanup:
    def __init__(self, file_name="202204.txt", file_reader=FileReader()):
        self.assignments = file_reader.read_txt(file_name)

    def find_fully_overlapping(self):
        overlapping_count = 0

        for one, two in self.assignments:
            print(one, two)

        return overlapping_count
