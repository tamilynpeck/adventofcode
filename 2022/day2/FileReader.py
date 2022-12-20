class FileReader:
    def __init__(self):
        pass

    @staticmethod
    def read_txt(file):
        with open(file) as input_file:
            data = [line.strip() for line in input_file.readlines()]

        return data
