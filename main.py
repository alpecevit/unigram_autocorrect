import os
from classes.EditDistance import EditDistance
from functions.check_user_input import check_user_input
from functions.corpus_path_exists import corpus_path_exists
from functions.read_corpus_file import read_corpus_file

# Data source: https://github.com/hackerb9/gwordlist/tree/master
PATH = os.path.join(os.getcwd(), "data", "ngram.txt")

# Example inputs you can try:
# 1. How big is the feild
# 2. I have been wating fot you
# 3. I am going to the parkk
# 4. Beklava is my favorite dessert
# 5. The coach smiled at the player who tossed the frisbe
while True:
    user_inp = input("Please enter a text with alpha characters where words "
                     "are seperated by single whitespace: ").strip()
    is_valid = check_user_input(user_inp)
    if is_valid:
        break
    else:
        print("Please enter a valid input that consists of alpha characters.")

if corpus_path_exists(PATH):
    word_dict = read_corpus_file(PATH)
    edit_instance = EditDistance(word_dict)
    sentence = []
    for word in user_inp.split():
        # Here I am checking if the word is longer than 2 characters, if so,
        # I am passing it to the get_candidate function, otherwise I am
        # appending it to the sentence list as it is.
        if len(word) > 2:
            cand = edit_instance.get_candidate(word.lower())
            # Here I am doing additional check to see if the word is
            # capitalized.
            if word[0].isupper():
                sentence.append(cand.capitalize())
            else:
                sentence.append(cand)
        else:
            sentence.append(word)
    print(' '.join(sentence))
else:
    print(f"File not found at: {PATH}")
