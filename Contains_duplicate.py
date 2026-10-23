def contains_duplicate(input_list: list) -> bool:
    return not(len(input_list) == len(set(input_list)))

assert contains_duplicate([1,2,3,4]) == False
assert contains_duplicate([]) == False
assert contains_duplicate([1,1,3,4]) == True
assert contains_duplicate([0, 0]) == True
assert contains_duplicate([1,2,3,'']) == False