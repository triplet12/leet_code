def two_sum(nums: list[int], targer: int) -> list[int, int] | None:
    i = 0
    j = -1
    for _ in range(len(nums)):
        print(i,j, len(nums))
        if (nums[i] + nums[j]) == targer:
            return(i, len(nums) - 1)
        if (nums[i] + nums[j]) > targer:
            j -= 1
        if (nums[i] + nums[j]) < targer:
                    i += 1
    return None
