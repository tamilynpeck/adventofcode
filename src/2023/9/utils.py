def read_file(path):
    with open(path) as f:
        return f.read().splitlines()


def read_file_as_text(path):
    with open(path) as f:
        return f.read()


def read_txt(text_data):
    return text_data.splitlines()
