def findMajority(arr):
    n=len(arr)
    freq = {}
    res = []
    for ele in arr:
        freq[ele] = freq.get(ele , 0) + 1
    for key,value in freq.items():
        if value > n//3:
            res.append(key)
    if len(res) == 2 and res[0] > res[1]:
        res[0],res[1] = res[1],res[0]
    return res

arr = [2,2,3,1,3,2,1,3]
print(findMajority(arr))