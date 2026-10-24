def palindrome(input_string: str) -> bool:
    '''Время O(n), память O(1)'''
    
    left = 0
    right = len(input_string) - 1
    input_string = input_string.lower()
    while left < right:
        if not input_string[right].isalnum():
            right -= 1
            continue
        if not input_string[left].isalnum():
            left += 1
            continue
        elif input_string[right] != input_string[left]:
            return False
        
        right -=1
        left += 1
    return True

