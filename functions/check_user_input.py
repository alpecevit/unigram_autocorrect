def check_user_input(user_str):
    """
    A function that checks if the input word is consisted of alpha characters.
    If all characters are alpha, returns True, False otherwise.
    """
    words = user_str.split()
    alpha_words = [w for w in words if w.isalpha()]
    if len(words) == len(alpha_words):
        return True
    else:
        return False


if __name__ == "__main__":
    assert check_user_input("123") is False
    assert check_user_input("hello there") is True
    assert check_user_input("hello 123") is False
