from string import ascii_lowercase, ascii_uppercase


class Priority:
    letters = ascii_lowercase + ascii_uppercase

    @staticmethod
    def get_priority(item):
        return Priority.letters.index(item) + 1


class Rucksack:
    def __init__(self, contents):
        pocket_size = len(contents) // 2
        self.contents = contents
        self.compartments = [contents[:pocket_size], contents[pocket_size:]]

    def find_duplicate_item(self):
        for item in self.compartments[0]:
            if item in self.compartments[1]:
                return item


class RucksackGroup:
    def __init__(self, rucksacks):
        self.rucksacks = [Rucksack(sack) for sack in rucksacks]

    def find_shared_item(self):
        for item in self.rucksacks[0].contents:
            if (
                item in self.rucksacks[1].contents
                and item in self.rucksacks[2].contents
            ):
                return item


class RunsackReorganization:
    def __init__(
        self,
        data,
        runsack=Rucksack,
        group=RucksackGroup,
        priority=Priority,
    ):
        self.rucksacks = data
        self.runsack = runsack
        self.group = group
        self.priority = priority

    def duplicate_item_priority_sum(self):
        priority_sum = 0

        for sack in self.rucksacks:
            item = Rucksack(sack).find_duplicate_item()
            priority_sum += self.priority.get_priority(item)

        return priority_sum

    def group_badge_item_priority_sum(self):
        priority_sum = 0

        for sack in range(0, len(self.rucksacks), 3):
            rucksacks = self.rucksacks[sack : sack + 3]
            group = RucksackGroup(rucksacks)
            item = group.find_shared_item()
            # print(item)
            priority_sum += self.priority.get_priority(item)
            # print(rucksacks, priority_sum)

        return priority_sum
