class Day5:
    def __init__(self, data):
        self.data = data
        self.rules = [x for x in data if "|" in x]
        self.rules = [x.split("|") for x in self.rules]
        self.updates = [x for x in data if x and "|" not in x]
        self.updates = [x.split(",") for x in self.updates]

    def solve_part_one(self):
        valid_updates = []
        for update in self.updates:
            result = self.check_rules(update)
            if result:
                valid_updates.append(update[len(update) // 2])
        return sum([int(x) for x in valid_updates])

    def solve_part_two(self):
        valid_updates = []
        for update in self.updates:
            if not self.check_rules(update):
                result = self.correct_order(update)
                valid_updates.append(result[len(result) // 2])
        return sum([int(x) for x in valid_updates])

    def check_rules(self, update):
        for before, after in self.rules:
            before_index = update.index(before) if before in update else -1
            after_index = update.index(after) if after in update else -1
            if (
                before_index > -1
                and after_index > -1
                and not before_index < after_index
            ):
                return False
        return True

    def map_rules(self):
        distinct_values = set([x for y in self.rules for x in y])
        mapped_rules = {value: [] for value in distinct_values}
        for rule in self.rules:
            mapped_rules[rule[0]].append(rule[1])
        return mapped_rules

    def correct_order(self, update):
        update_map = {}
        for value in update:
            update_map[value] = [x for x in self.map_rules()[value] if x in update]

        return sorted(update_map.keys(), key=lambda k: -len(update_map[k]))
