from common.FileReader import FileReader


class Elf:
    def __init__(self, elf_number):
        self.elf_number = elf_number
        self.item_calories = []

    def additional_item(self, item):
        self.item_calories.append(item)

    def total_calories(self):
        # print(self.item_calories)
        return sum(self.item_calories)


def calorie_counting(input_file, top=1):
    input = FileReader.read_txt(input_file)
    data = [int(line) if line.isnumeric() else None for line in input]

    elves = []
    for item in data:
        if len(elves) == 0:
            elves.append(Elf(len(elves)))

        if item:
            elves[len(elves) - 1].additional_item(item)
        else:
            new_elf = Elf(len(elves))
            elves.append(new_elf)

    # sort by total
    totals = [elf.total_calories() for elf in elves]

    totals.sort(reverse=True)
    return sum(totals[0:top])
