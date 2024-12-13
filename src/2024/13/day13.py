class Day13:
    def __init__(self, data):
        self.data = []
        for i, line in enumerate(data):
            if not line.startswith("Button A"):
                continue
            claw_machine = ClawMachine()

            button_a = line.split(": ")[1].split(", ")
            button_b = data[i + 1].split(": ")[1].split(", ")
            prize = data[i + 2].split(": ")[1].split(", ")
            claw_machine.a = (
                int(button_a[0].split("+")[1]),
                int(button_a[1].split("+")[1]),
            )
            claw_machine.b = (
                int(button_b[0].split("+")[1]),
                int(button_b[1].split("+")[1]),
            )
            claw_machine.prize = (
                int(prize[0].split("=")[1]),
                int(prize[1].split("=")[1]),
            )
            self.data.append(claw_machine)
        print(self.data)

    def solve_part_one(self):
        results = []
        for claw in self.data:
            result = self.evaluate_claw_machine(claw)
            if result:
                results.append(result)

        return sum(results)

    def solve_part_two(self):
        for claw in self.data:
            claw.part_two_update()

        return self.solve_part_one()

    def evaluate_claw_machine(self, claw):
        # Coefficients for the equations
        a1, b1, c1 = claw.a[0], claw.b[0], claw.prize[0]
        a2, b2, c2 = claw.a[1], claw.b[1], claw.prize[1]

        # Calculate the determinant of the coefficient matrix
        det = a1 * b2 - a2 * b1
        if det == 0:
            return None

        # Calculate the determinants for the numerators
        det_a = c1 * b2 - c2 * b1
        det_b = a1 * c2 - a2 * c1

        # Solve for A and B using Cramer's rule
        a_presses = det_a // det
        b_presses = det_b // det

        if claw.prize[0] != a_presses * claw.a[0] + b_presses * claw.b[0]:
            return None
        if claw.prize[1] != b_presses * claw.b[1] + a_presses * claw.a[1]:
            return None

        # Calculate the total cost
        total_cost = 3 * a_presses + 1 * b_presses
        print(f"Total cost to win the prize: {total_cost} tokens")

        return total_cost


class ClawMachine:
    def __init__(self):
        self.a = (0, 0)
        self.b = (0, 0)
        self.prize = (0, 0)

    def part_two_update(self):
        self.prize = (self.prize[0] + 10000000000000, self.prize[1] + 10000000000000)

    def __repr__(self):
        return f"<Button A: {self.a}\nButton B: {self.b}\nPrize: {self.prize}>"
