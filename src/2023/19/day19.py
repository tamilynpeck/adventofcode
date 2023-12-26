class Day19:
    def __init__(self, data):
        workflows = [l for l in data if l != "" and not l.startswith("{")]
        self.workflows = self.parse_workflows(workflows)
        self.ratings = [
            self.parse_ratings(line) for line in data if line.startswith("{")
        ]

    def parse_rule_function(self, rule):
        if ":" not in rule:
            return lambda rating: rule

        check, workflow = rule.split(":")
        if ">" in check:
            part, value = check.split(">")
            return lambda rating: workflow if int(rating[part]) > int(value) else False
        if "<" in check:
            part, value = check.split("<")
            return lambda rating: workflow if int(rating[part]) < int(value) else False

    def parse_workflows(self, lines):
        workflows = {}
        for line in lines:
            key, value = line.strip("}").split("{")
            workflows[key] = [self.parse_rule_function(r) for r in value.split(",")]

        return workflows

    def parse_ratings(self, line):
        ratings = line.strip("{}").split(",")
        ratings = [r.split("=") for r in ratings]
        return {k: int(v) for k, v in ratings}

    def solve_part_one(self):
        accepted_ratings = []
        for rating in self.ratings:
            result = self.sort_rating(rating, "in")
            if result:
                accepted_ratings.append(rating)

        values = [sum(r.values()) for r in accepted_ratings]
        return sum(values)

    def sort_rating(self, rating, workflow):
        rules = self.workflows[workflow]
        for rule in rules:
            result = rule(rating)
            if result in self.workflows.keys():
                return self.sort_rating(rating, result)
            if result == "A":
                return True
            if result == "R":
                return False

    def solve_part_two(self):
        rating_ranges = {
            "x": (1, 4001),
            "m": (1, 4001),
            "a": (1, 4001),
            "s": (1, 4001),
        }
