class CubeConundrum:
    def __init__(self, data):
        self.data = data
        self.games = [CubeGame(game) for game in self.data]

    def possible_games(self, red, green, blue):
        possible_games_id = []
        for game in self.games:
            if game.high_red <= red and game.high_green <= green and game.high_blue <= blue:
                possible_games_id.append(game.game_id)
        return sum(possible_games_id)
    
    def power(self):
        return sum([game.high_red * game.high_green * game.high_blue for game in self.games])
    

class CubeGame: 
    def __init__(self, game):
        number, turn_data = game.split(":")
        self.game_id = int(number.split(" ")[1])
        turn_data = turn_data.split(";")
        turn_text = [turn.split(",") for turn in turn_data]

        self.turns = [TurnSet.parse_set(turn) for turn in turn_text]

        
        self.high_red = max([turn.red for turn in self.turns])
        self.high_green = max([turn.green for turn in self.turns])
        self.high_blue = max([turn.blue for turn in self.turns])

class TurnSet:
    def __init__(self, turn_set):
        self.red = 0
        self.green = 0
        self.blue = 0

        for set in turn_set:
            number, color = set
            if color == "red":
                self.red = int(number)
            elif color == "green":
                self.green = int(number)
            elif color == "blue":
                self.blue = int(number)
            else:
                raise ValueError(f"unknown color {color}")


    def parse_set(turn):
        sets = [set.strip().split(" ") for set in turn]

        turn_set = TurnSet(sets)
        

        return turn_set

    def __repr__(self) -> str:
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"