def contains_duplicate(input_list: list) -> bool: 
    '''Сложность по времени O(n)
    Сложность по памяти O(n)'''
    return not(len(input_list) == len(set(input_list)))
