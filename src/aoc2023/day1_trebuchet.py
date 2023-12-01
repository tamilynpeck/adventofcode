TEXT_NUMBER_KEY = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


class Trebuchet:
    def __init__(self, data):
        self.data = data

    def calibrate_sum(self):
        return sum([Trebuchet.calibration_value(line) for line in self.data])

    def calibrate_sum_after_interpreting_data(self):
        interpret_data = [Trebuchet.interpret_line(line) for line in self.data]
        return sum([Trebuchet.calibration_value(line) for line in interpret_data])

    def sum(self):
        return sum([Trebuchet.calibration_value(line) for line in self.data])

    @staticmethod
    def calibration_value(line):
        numbers = [int(char) for char in line if char.isdigit()]
        if not numbers:
            raise ValueError(f"no numbers in {line}")
        return int(f"{numbers[0]}{numbers[-1]}")

    @staticmethod
    def interpret_line(line):
        result = ""
        for i, _ in enumerate(line):
            result += Trebuchet.find_text_number(line[i:])

        return result

    @staticmethod
    def find_text_number(line):
        result = ""
        for key, value in TEXT_NUMBER_KEY.items():
            if line.find(key) == 0:
                return value

        return result
