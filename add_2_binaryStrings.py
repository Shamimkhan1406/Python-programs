def treamLeadingZeros(s):
    firstOne = s.find('1')
    return s[firstOne:] if firstOne != -1 else '0'
def addBinaryStrings(s1,s2):
    s1 = treamLeadingZeros(s1)
    s2 = treamLeadingZeros(s2)
    n = len(s1)
    m = len(s2)
    if n < m:
        s1,s2 = s2,s1
        n,m = m,n
    j = m-1
    carry = 0
    res = []
    for i in range (n-1,-1,-1):
        bit1 = int(s1[i])
        bitSum = bit1 + carry
        if j >= 0:
            bit2 = int(s2[j])
            bitSum += bit2
            j -= 1
        bit = bitSum % 2
        carry = bitSum // 2
        res.append(str(bit))
    if carry> 0:
        res.append('1')
    res.reverse()
    return ''.join(res)

s1 = "1101"
s2 = "111"
print(addBinaryStrings(s1,s2))  # Output: "10100"
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m)) for the result string
# This code implements the addition of two binary strings, handling leading zeros and carry-over.
# It trims leading zeros from both strings, ensures the longer string is processed first, and adds the bits together while managing carry.
# The result is built in reverse order and then reversed back to get the final binary sum.
# The function returns the sum as a binary string.
