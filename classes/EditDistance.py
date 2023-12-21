class EditDistance:
    """
    A class that takes a corpus as an input and returns the most 
    probable corrected word.
    """

    def __init__(self, corpus):
        """
        Initialize EditDistance with the provided corpus.
        """
        self.corpus = corpus

    def __damerau_levenshtein_distance(self, str1, str2):
        """
        A private method that takes two strings and returns the Damerau-
        Levenshtein distance between them.
        """
        len_str1, len_str2 = len(str1), len(str2)
        matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        for i in range(len_str1 + 1):
            matrix[i][0] = i

        for j in range(len_str2 + 1):
            matrix[0][j] = j

        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1] + cost,
                )
                if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and \
                str1[i - 2] == str2[j - 1]:
                    matrix[i][j] = min(matrix[i][j], 
                                       matrix[i - 2][j - 2] + cost)  

        return matrix[len_str1][len_str2]

    def get_candidate(self, inp_str):
        """
        A public method that takes in an input string and returns the most
        probable corrected word as string.
        """
        if inp_str in self.corpus:
            return inp_str
        else:
            candidate_dict= {}
            for key, value in self.corpus.items():
                distance = self.__damerau_levenshtein_distance(inp_str, key)
                candidate_dict[key] = (distance, value)
            # checking if there are
            min_edit_dist = min(value[0] for _, value in candidate_dict.items())
            if min_edit_dist < 3:
                most_probable_word = sorted(candidate_dict.items(), 
                                            key=lambda x: (x[1][0], 
                                                           -x[1][1]))[0][0]
            else:
                # If the edit distance between found candidates and input word
                # is higher than 5, provide a fallback suggestion which is to 
                # return the input string itself
                most_probable_word = inp_str
            return most_probable_word

    def __repr__(self):
        """
        Returns a string representation of the EditDistance object.
        """
        if self.corpus and len(self.corpus) > 4:
            beginning = (str(dict(list(self.corpus.items())[:2]))
                         .replace('{', '').replace('}', ''))
            end = (str(dict(list(self.corpus.items())[-2:]))
                   .replace('{', '').replace('}', ''))
            trunc_dict = "{" + beginning + ', ... ' + end + "}"
        elif 0 < len(self.corpus) <= 4:
            trunc_dict = f"{self.corpus}"
        else:
            trunc_dict = "{}"
        return (f"EditDistance({trunc_dict})")


if __name__ == "__main__":
    # Test get_candidate() method
    corpus = {"apple": 1, "banana": 2, "orange": 3}
    edit_distance = EditDistance(corpus)
    
    assert edit_distance.get_candidate("appl") == "apple"
    assert edit_distance.get_candidate("banan") == "banana"
    assert edit_distance.get_candidate("orng") == "orange"
    assert edit_distance.get_candidate("grape") == "grape"
    assert edit_distance.get_candidate("formula") == "formula"
