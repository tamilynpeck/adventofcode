class SpaceAnalyzer:
    def __init__(self, data):
        self.commands = data
        self.directories = self.group_directories()
        self.max_size = 70000000
        self.min_unused_size_needed = 30000000
        self.unused_size = lambda max, current: max - current

    def solve_part_one(self):
        return self.get_small_directories()

    def solve_part_two(self):
        return self.find_directory_to_delete()

    def group_directories(self):
        directories = {}
        current_dirs = []

        for command in self.commands:
            command = command.replace("$ ", "")
            commands = command.split(" ", 1)
            if len(commands) < 2:
                continue
            size, dir = commands
            if command == "cd .." and current_dirs:
                current_dirs.pop()
            elif command.startswith("cd"):
                next_dir = current_dirs[-1] + "-" + dir if current_dirs else dir
                if next_dir not in current_dirs:
                    current_dirs.append(next_dir)
                if next_dir not in directories:
                    directories[next_dir] = 0
            elif size.isnumeric():
                for dir in current_dirs:
                    directories[dir] += int(size)

        return directories

    def get_small_directories(self):
        small_directories = [
            value for value in self.directories.values() if value <= 100000
        ]
        return sum(small_directories)

    def find_directory_to_delete(self):
        current_size = self.directories["/"]
        sorted_directories = sorted(self.directories.values())

        for value in sorted_directories:
            if (
                self.unused_size(self.max_size, current_size - value)
                >= self.min_unused_size_needed
            ):
                return value
