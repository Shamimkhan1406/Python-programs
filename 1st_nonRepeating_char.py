#MAX_CHAR = 26

def nonRep(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0)+1
    for i in freq:
        if freq[i] == 1:
            return i
    return '$'

s = "holaho"
print(nonRep(s))
