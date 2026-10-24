def first_unique_char(input_string: str) -> int | None:
    '''Время O(n), Память O(n)'''
    char_vocab: dict[str, int] = {}
    for char in input_string:
        char_vocab[char] = char_vocab.get(char, 0) + 1


    for char, value in char_vocab.items():
        if value == 1:
            return input_string.find(char)
    return None
        