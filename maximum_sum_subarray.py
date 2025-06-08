def maxSumSubarray(arr):
    res = arr[0]
    max_ending = arr[0]
    for i in range(1,len(arr)):
        max_ending = max(arr[i]+max_ending, arr[i])
        res = max(res, max_ending)
    return res
arr = [2,3,-8,7,-1,2,3]
print(maxSumSubarray(arr))  
# Time Complexity: O(n)
# Space Complexity: O(1) as we are using only a few extra variables
# This code implements Kadane's algorithm to find the maximum sum of a contiguous subarray.