def largest_area_histogram(arr):
    ans = -1
    i = j = 0
    stack = []
    area = 0

    while i < len(arr):
        if len(stack) == 0 or arr[i] >= arr[stack[0]]:
            stack.insert(0, i)
            i = i + 1
        else:
            top = stack.pop(0)
            if len(stack) == 0:
                area = stack[top] * i
            else:
                while arr[i] > arr[top]:
                    area = arr[top] * (i - top - 1)
    return ans

array = [1, 2, 5, 2]
print(largest_area_histogram(array))