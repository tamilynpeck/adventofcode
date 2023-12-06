class BinaryDiagnostic:
    def __init__(self, input):
        self.input = input
        self.gamma = ""
        self.epsilon = ""
        self.oxygen_generator_rating = ""
        self.c02_scrubber = ""
        self.calculate()
        self.power_consumption  = int(self.gamma, 2) * int(self.epsilon, 2)
        self.life_support_rating = int(self.oxygen_generator_rating, 2) * int(self.c02_scrubber, 2)


    @staticmethod
    def most_common(input, tie_breaker = None):
        if tie_breaker and input.count('0') == input.count('1'):
            return tie_breaker
        return '0'  if input.count('0') > input.count('1') else '1'

    @staticmethod
    def least_common(input, tie_breaker = None):
        if tie_breaker and input.count('0') == input.count('1'):
            return tie_breaker
        return '0'  if input.count('0') < input.count('1') else '1'

    def calculate(self):
        loops = len(self.input[0])
        remaining_inputs_oxygen = self.input
        remaining_inputs_c02 = self.input
        print(remaining_inputs_oxygen)
        print(remaining_inputs_c02)
        for position in range(0,loops):
            chars = [char for row in self.input for char in row[position]]
            # most_common = '0'  if chars.count('0') > chars.count('1') else '1'
            # least_common = '0'  if chars.count('0') < chars.count('1') else '1'

            self.gamma += self.most_common(chars)
            self.epsilon += self.least_common(chars)


            oxygen_chars = [char for row in remaining_inputs_oxygen for char in row[position]]
            c0x_chars = [char for row in remaining_inputs_c02 for char in row[position]]

            oxygen_most_common = self.most_common(oxygen_chars, '1')
            c0x_least_common = self.least_common(c0x_chars, '0')

            if len(remaining_inputs_oxygen) > 1:
                remaining_inputs_oxygen = [row for row in remaining_inputs_oxygen if row[position] == oxygen_most_common]
            if len(remaining_inputs_c02) > 1:
                remaining_inputs_c02 = [row for row in remaining_inputs_c02 if row[position] == c0x_least_common]
            
            print("position", position)
            print(oxygen_most_common, remaining_inputs_oxygen)
            print(c0x_least_common, remaining_inputs_c02)
        self.oxygen_generator_rating = remaining_inputs_oxygen[0] if remaining_inputs_oxygen else None
        self.c02_scrubber = remaining_inputs_c02[0] if remaining_inputs_c02 else None

        

