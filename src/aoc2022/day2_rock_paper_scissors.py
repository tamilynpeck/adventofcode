from common.FileReader import FileReader


class GameManager:
    winner_of_action = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    loser_of_action = {v: k for k, v in winner_of_action.items()}

    @staticmethod
    def result_of_actions(opponent_action, action):
        if opponent_action == action:
            return "Draw"

        if GameManager.winner_of_action.get(action) == opponent_action:
            return "Win"

        return "Lose"

    @staticmethod
    def action_for_expected_result(opponent_action, expected_result):
        print(opponent_action, expected_result)
        if expected_result == "Draw":
            return opponent_action

        if expected_result == "Win":
            return GameManager.winner_of_action.get(opponent_action)

        if expected_result == "Lose":
            return GameManager.loser_of_action.get(opponent_action)


class ScoreCalculator:
    score_mapping = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
        "Lose": 0,
        "Draw": 3,
        "Win": 6,
    }

    @staticmethod
    def score(action, result):
        if not action or not result:
            raise Exception("score", action, result)
        return ScoreCalculator.score_mapping.get(
            action
        ) + ScoreCalculator.score_mapping.get(result)


class ActionsGuideEngine:
    opponent_action = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    action = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    def __init__(self, guide, calculator=ScoreCalculator, game_manager=GameManager):
        self.guide = guide
        self.calculator = calculator
        self.game_manager = game_manager

    def play(self):
        results = []
        for o, a in self.guide:
            opponent_action = self.opponent_action.get(o)
            action = self.action.get(a)
            result = self.game_manager.result_of_actions(opponent_action, action)
            results.append(self.calculator.score(action, result))

        return sum(results)


class ResultsGuideEngine:
    opponent_action = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    result_mapping = {"X": "Lose", "Y": "Draw", "Z": "Win"}

    def __init__(self, guide, calculator=ScoreCalculator, game_manager=GameManager):
        self.guide = guide
        self.calculator = calculator
        self.game_manager = game_manager

    def play(self):
        results = []
        for o, r in self.guide:
            opponent_action = self.opponent_action.get(o)
            result = self.result_mapping.get(r)
            action = self.game_manager.action_for_expected_result(
                opponent_action, result
            )
            results.append(self.calculator.score(action, result))

        return sum(results)


def rock_paper_scissors(
    input_file,
    guide_type="actions",
    file_reader=FileReader(),
):
    data = file_reader.read_txt(input_file)
    guide = [[line[0], line[2]] for line in data]

    guide_engine = get_guide_engine(guide_type)(guide)

    score = guide_engine.play()

    return score


def get_guide_engine(guide_type):
    if guide_type == "actions":
        return ActionsGuideEngine
    if guide_type == "results":
        return ResultsGuideEngine

    raise ValueError("Unknown guide type")
