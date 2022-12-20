from FileReader import FileReader


# Rock defeats Scissors, Scissors defeats Paper, Paper defeats Rock
class Score:
    opponent_mapping = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    personal_mapping = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
    personal_mapping = {"X": "Lose", "Y": "Draw", "Z": "Win"}
    score_mapping = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
        "Lost": 0,
        "Draw": 3,
        "Win": 6,
    }
    rules = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

    @staticmethod
    def score(opponent, personal):
        score = 0
        opponent = Score.opponent_mapping.get(opponent)
        personal = Score.personal_mapping.get(personal)

        score += Score.score_mapping.get(personal)

        if opponent == personal:
            score += Score.score_mapping.get("Draw")

        if Score.rules.get(personal) == opponent:
            score += Score.score_mapping.get("Win")

        if Score.rules.get(opponent) == personal:
            score += Score.score_mapping.get("Lost")

        return score


def rock_paper_scissors(input_file):
    data = FileReader.read_txt(input_file)
    guide = [[line[0], line[2]] for line in data]
    print(guide)
    score = 0

    for round in guide:
        score += Score.score(round[0], round[1])

    return score


if __name__ == "__main__":
    PUZZLE_INPUT_FILE = "input.txt"
    result = rock_paper_scissors(PUZZLE_INPUT_FILE)
    print(result)
