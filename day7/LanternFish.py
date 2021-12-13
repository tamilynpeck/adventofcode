import math


class LanternFish:
    def __init__(self, input):
        self.input = input

    def days(self, days):
        sea = self.input.copy()
        for day in range(0, days):
            for i in range(0, len(sea)):
                if sea[i] == 0:
                    sea[i] = 6
                    sea.append(8)
                else:
                    sea[i] -= 1
        return len(sea)

    def better_days(self, days):
        sea = len(self.input)
        print(self.input)
        for fish in self.input:
            f = int(math.ceil((days - fish) / 7))
            print(f)
            sea += f

        print(sea)
        return sea
