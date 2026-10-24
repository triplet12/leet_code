def palindrome(input_string: str) -> bool:
    '''Время O(n), память O(1)'''
    for i in range(len(input_string) // 2):
        if input_string[i] != input_string[-i - 1]:
            return False
    return True

assert palindrome('12321') == True
assert palindrome('') == True
assert palindrome('0') == True
assert palindrome('12420') == False