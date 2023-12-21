import os


def read_corpus_file(file_path):
    """
    A function for reading the word probability corpus text file and returning
    a dictionary where keys are words and values are counts.
    """
    word_counts = {}
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)

        for line in file:
            # Split the line into columns
            columns = line.strip().split()

            # Extract word and count
            keyword = columns[1].lower()
            count = int(columns[2].replace(',', ''))
            # Add the word and count to the dictionary if the word is longer
            # than two characters
            if len(keyword) > 2:
                word_counts[keyword] = count

    return word_counts


if __name__ == "__main__":
    corpus_path = os.path.join('..', 'data', 'ngram.txt')
    assert isinstance(read_corpus_file(corpus_path), dict)
