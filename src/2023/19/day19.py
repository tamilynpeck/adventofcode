class Day19:
    def __init__(self, data):
        workflows = [l for l in data if l != "" and not l.startswith("{")]
        self.workflows = self.parse_workflows(workflows)
        self.ratings = [
            self.parse_ratings(line) for line in data if line.startswith("{")
        ]

    def solve_part_one(self):
        accepted_ratings = []
        for rating in self.ratings:
            result = self.sort_rating(rating, "in")
            if result:
                accepted_ratings.append(rating)

        values = [sum(r.values()) for r in accepted_ratings]
        return sum(values)

    def solve_part_two(self):
        pass

    def sort_rating(self, rating, workflow):
        print(rating, workflow)
        rules = self.workflows[workflow]
        for rule in rules:
            result = self.parse_rule(rating, rule)
            print(rule, result)
            if result == "A":
                return True
            if result == "R":
                return False
            if result in self.workflows.keys():
                return self.sort_rating(rating, result)

    def parse_rule(self, rating, rule):
        if ":" not in rule:
            return rule

        check, workflow = rule.split(":")
        if ">" in check:
            part, value = check.split(">")
            if int(rating[part]) > int(value):
                return workflow
        if "<" in check:
            part, value = check.split("<")
            if int(rating[part]) < int(value):
                return workflow

    def parse_workflows(self, lines):
        workflows = {}
        for line in lines:
            key, value = line.strip("}").split("{")
            workflows[key] = value.split(",")

        return workflows

    def parse_ratings(self, line):
        ratings = line.strip("{}").split(",")
        ratings = [r.split("=") for r in ratings]
        return {k: int(v) for k, v in ratings}
