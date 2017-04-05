
def short_all_char(strn):
    dic = {}
    st = set(strn)
    start = end = 0

    count = 0
    for i in range(len(strn)):
        if dic.get(strn[i], None) is None:
            count = count + 1
            dic[strn[i]] = 1
            if count == len(st):
                start = i
        else:
            dic[strn[i]] = dic[strn[i]] + 1

    ans = end - start + 1

    print(ans)
    print(range(end, len(strn)))
    while dic[strn[start]] > 1:
        dic[strn[start]] = dic[strn[start]] - 1
        start = start + 1
        ans = min(ans, end - start + 1)
    for i in range(end+1, len(strn)):
        while dic[strn[start]] > 1:
            dic[strn[start]] = dic[strn[start]] - 1
            start = start + 1
            ans = min(ans, end - start + 1)
        end = i
        dic[strn[end]] = dic.get(strn[end], 0) + 1
    return ans

print(short_all_char("aabbcc"))

