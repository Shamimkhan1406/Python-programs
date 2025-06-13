def circularSubArraySum(arr):
    curMaxSum = 0
    curMinSum = 0
    totalSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    for i in range(len(arr)):
        curMaxSum = max(curMaxSum + arr[i], arr[i])
        maxSum = max(maxSum,curMaxSum)
        curMinSum = min(curMinSum +arr[i],arr[i])
        minSum = min(minSum,curMinSum)
        totalSum += arr[i]
    normalSum = maxSum
    circularSum = totalSum - minSum
    if totalSum == minSum:
        return normalSum
    return max(normalSum,circularSum)

arr = [8,-8,9,-9,10,-11,12]
print(circularSubArraySum(arr))  # Output: 22
# Time Complexity: O(n)
# Space Complexity: O(1) as we are using only a few extra variables
# This code implements a solution to find the maximum sum of a circular subarray.
# It uses Kadane's algorithm to find both the maximum and minimum subarray sums,
# and then calculates the total sum of the array to determine the maximum circular subarray sum.    