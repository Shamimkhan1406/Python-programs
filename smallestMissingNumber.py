
def smallestMissingNumber(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i]-1]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
    for i in range(1,n+1):
        if arr[i-1]!= i:
            return i
    return n + 1

arr = [2,-3,4,1,1,7]
print(smallestMissingNumber(arr))
# Time Complexity: O(n)
# Space Complexity: O(1)
# This code finds the smallest missing positive integer in an array.
# It rearranges the array such that each positive integer is placed at its corresponding index.
# If an integer is missing, it returns the smallest missing positive integer.
# If all integers from 1 to n are present, it returns n + 1.
            