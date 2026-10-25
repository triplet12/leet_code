def top_k_freq(nums :list[int], k:int) -> list[int]:
    dict_of_nums = {}
    for num in nums:
        dict_of_nums[num] = dict_of_nums.get(num, 0) + 1
    return sorted(dict_of_nums, key=dict_of_nums.get, reverse=True)[:k]

