from common.FileReader import FileReader


class ScoreCalculator:
    winner_of_action = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    loser_of_action = {v: k for k, v in winner_of_action.items()}

    def __init__(self):
        self.action_mapping = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors",
            "X": "Rock",
            "Y": "Paper",
            "Z": "Scissors",
        }
        self.result_mapping = {"X": "Lose", "Y": "Draw", "Z": "Win"}
        self.score_mapping = {
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3,
            "Lost": 0,
            "Draw": 3,
            "Win": 6,
        }

    def score(self, first_value, second_value):
        score = 0
        opponent_action = self.action_mapping.get(first_value)
        action = self.action_mapping.get(second_value)

        score += self.score_mapping.get(action)

        result = self.result_of_actions(opponent_action, action)
        score += self.score_mapping.get(result)

        return score

    def result_of_actions(self, opponent_action, action):
        if opponent_action == action:
            return "Draw"

        if self.winner_of_action.get(action) == opponent_action:
            return "Win"

        "Lost"

    def score_part2(self, first_value, second_value):
        score = 0
        opponent_action = self.action_mapping.get(first_value)
        expected_result = self.result_mapping.get(second_value)
        print(expected_result)

        score += self.score_mapping.get(expected_result)

        expected_action = ScoreCalculator.action_for_expected_result(
            opponent_action, expected_result
        )
        score += self.score_mapping.get(expected_action)

        return score

    def action_for_expected_result(opponent_action, expected_result):
        if expected_result == "Draw":
            return opponent_action

        if expected_result == "Win":
            return ScoreCalculator.winner_of_action.get(expected_result)

        if expected_result == "Lost":
            return ScoreCalculator.loser_of_action.get(expected_result)


def rock_paper_scissors(input_file, default_calc=True):
    data = FileReader.read_txt(input_file)
    guide = [[line[0], line[2]] for line in data]

    calculator = ScoreCalculator()
    score = 0

    for round in guide:
        score += (
            calculator.score(round[0], round[1])
            if default_calc
            else calculator.score_part2(round[0], round[1])
        )

    return score
