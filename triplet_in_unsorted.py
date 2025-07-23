"""
Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0
Input: arr[] = [2, 3, 1, 0, 5]
Output: [[]]
Explanation: There is no triplet with sum 0.
"""
# brute force approach
# time complexity: O(n^3)
# space complexity: O(1)

def findTriplet(arr):
    res = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    res.append([i,j,k])
    return res

# using sets and map
# time complexity: O(n^3)
# space complexity: O(n)
def _findTriplet(arr):
    res = set()
    map = {}
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            sum = arr[i]+arr[j]
            if sum not in map:
                map[sum] = []
                #map[sum].append([i,j])
            map[sum].append((i,j))
    for i in range(n):
        rem = -arr[i]
        if rem in map:
            for p in map[rem]:
                if p[0] != i and p[1] != i:
                    res.add(tuple(sorted([p[0],p[1],i])))
    return [list(x) for x in res]


if __name__ == "__main__":
    arr =  [0, -1, 2, -3, 1]
    print(_findTriplet(arr)) # [[0, 1, 4], [2, 3, 4]]