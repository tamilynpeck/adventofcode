class CubeConundrum:
    def __init__(self, data):
        self.data = data
        self.games = [CubeGame(game) for game in self.data]

    def possible_games(self, red, green, blue):
        possible_games_id = [
            game.game_id
            for game in self.games
            if game.max_red <= red and game.max_green <= green and game.max_blue <= blue
        ]

        return sum(possible_games_id)

    def power(self):
        return sum(
            [game.max_red * game.max_green * game.max_blue for game in self.games]
        )


class CubeGame:
    def __init__(self, game):
        number, game_data = game.split(":")
        self.game_id = int(number.replace("Game", "").strip())

        cube_sets_data = [cube_set.split(",") for cube_set in game_data.split(";")]
        self.cube_sets = [CubeSet(cube_set) for cube_set in cube_sets_data]

        self.max_red = max([cubes.red for cubes in self.cube_sets])
        self.max_green = max([cubes.green for cubes in self.cube_sets])
        self.max_blue = max([cubes.blue for cubes in self.cube_sets])


class CubeSet:
    def __init__(self, cubes):
        self.cubes = CubeSet.parse_cubes(cubes)
        self.red = self.cubes.get("red", 0)
        self.green = self.cubes.get("green", 0)
        self.blue = self.cubes.get("blue", 0)

    @staticmethod
    def parse_cubes(cube_set):
        parsed_set = [set.strip().split(" ") for set in cube_set]
        return {color: int(number) for number, color in parsed_set}

    def __repr__(self) -> str:
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"
