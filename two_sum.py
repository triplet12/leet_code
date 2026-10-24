def two_sum(nums: list[int], targer: int) -> list[int, int] | None:
    i = 0
    j = len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) > targer:
            j -= 1
        elif (nums[i] + nums[j]) < targer:
            i += 1
        else: 
            print(i,j)
            return(i, j)
    return None

