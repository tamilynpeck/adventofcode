from common.FileReader import FileReader
from string import ascii_lowercase, ascii_uppercase

# https://adventofcode.com/2022/day/3


class Priority:
    letters = ascii_lowercase + ascii_uppercase

    @staticmethod
    def get_priority(item):
        return Priority.letters.index(item) + 1


class Rucksack:
    def __init__(self, contents):
        pocket_size = len(contents) // 2
        self.compartments = [contents[:pocket_size], contents[pocket_size:]]
        self.shared_item = self.find_shared_item()

    def find_shared_item(self):
        for item in self.compartments[0]:
            if item in self.compartments[1]:
                return item


def rucksack_reorganization(file_name="202203.txt", file_reader=FileReader()):
    rucksacks = file_reader.read_txt(file_name)

    priority_sum = 0

    for sack in rucksacks:
        item = Rucksack(sack).shared_item
        priority_sum += Priority.get_priority(item)
        print(sack, priority_sum)

    return priority_sum
