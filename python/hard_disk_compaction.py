def min_cost(arrayy):
    length = len(arrayy)
    ans = length + 1
    for i in range(len(arrayy)):
        cost = i + length - 1 - binary_search(arrayy, arrayy[i] + length - 1)
        # print(cost)
        ans = min(ans, cost)
    return ans


def binary_search(amr, num):
    start = 0
    end = len(amr) - 1
    while (end - start) > 1:
        mid = (start + end) // 2
        # print("start=", start," mid=", mid, " end=", end)
        if num > amr[mid]:
            start = mid
        else:
            end = mid
    if end - start == 1:
        if num > amr[end]:
            mid = end
        else:
            mid = start
    return mid

arr = [1, 2, 98, 99, 100]

# print(binary_search(arr, 5))

print("min cost = ", min_cost(arr))