def product_of_array(nums: list) -> list:

    left = [1]
    right = [1]
    result = []

    for i in range(1,len(nums)):
        left.append(nums[i-1] * left[i-1])

    for i in range(1,len(nums)):
        right.append(nums[-i] * right[i-1])

    for i in range(len(nums)):
        result.append(left[i] * right[len(nums) - i - 1])   

    return result

print(product_of_array([-1,1,0,-3,3]))