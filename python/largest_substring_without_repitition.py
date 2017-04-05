def lswr(strn):
    start = 0
    ans = -1
    dic = {}
    for i in range(len(strn)):
        if dic.get(strn[i], None) is None:
            dic[strn[i]] = i
        elif dic[strn[i]] >= start:
            start = dic[strn[i]] + 1
            dic[strn[i]] = i
        ans = max(ans,i-start+1)
    return ans


print(lswr("ssanydeepjjjzxcvbn"))