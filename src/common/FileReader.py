from pathlib import Path
import os


class FileReader:
    def __init__(self, base_path=os.getenv("WORKDIR", "input")):
        self.base_path = base_path

    def read_txt(self, file):
        file_path = Path(self.base_path, file)

        with open(file_path) as input_file:
            data = [line.strip() for line in input_file.readlines()]

        return data


class InMemoryFileReader:
    def __init__(self):
        self.files = {}

    def read_txt(self, file):
        if str(file) not in self.files:
            return None

        data = [line.strip() for line in self.files[file].splitlines()]

        return data

    def setup(self, file, data):
        self.files[file] = data
