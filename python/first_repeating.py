def first_repeating(nums):
    k = 1
    length = len(nums)
    for i in range(len(nums)):
        if nums[abs(nums[i]) % length] >= length:
            nums[abs(nums[i]) % length] = nums[abs(nums[i]) % length] * -1
        elif nums[abs(nums[i])%length] > 0:
            nums[abs(nums[i])%length] = nums[abs(nums[i])%length] + k * len(nums)
            k = k + 1
    temp = -99999999
    ans = -1
    for i in range(length):
        if nums[i] < 0:
            if temp < nums[i]:
                temp = nums[i]
                ans = i
    return ans

nums = [1, 2, 3, 3, 2, 4]

print(nums)
print(first_repeating(nums))
print(nums)