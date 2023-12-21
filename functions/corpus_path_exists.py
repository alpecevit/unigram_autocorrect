import os


def corpus_path_exists(corpus_path):
    """
    A function that takes file path string as an input and returns True if the
    file exists in that path, return False otherwise.
    """
    exists = True
    try:
        with open(corpus_path, 'r') as file:
            _ = file.read()
    except FileNotFoundError:
        exists = False
    return exists


if __name__ == "__main__":
    corp_path = os.path.join('..', 'data', 'ngram.txt')
    assert corpus_path_exists(corp_path) is True
