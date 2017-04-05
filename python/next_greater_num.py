def next_greater_num(nums):
    stack = [nums[-1]]
    ans = [-1 for i in range(len(nums))]

    for i in range(len(nums)-2, -1, -1):
        if len(stack) == 0:
            continue
        if nums[i] > stack[0]:
            while len(stack) > 0 and nums[i] > stack[0]:
                stack.pop(0)
            if len(stack) != 0:
                ans[i] = stack[0]
            stack.insert(0, nums[i])
        else:
            ans[i] = stack[0]
            stack.insert(0, nums[i])
    return ans

nums = [1, 2, 5, 3, 4, 9, 7, 6]
nums2 = [5, 8, 2, 3, 6]

print(next_greater_num(nums))
