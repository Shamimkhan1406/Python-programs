def maxProduct(arr):
    n=len(arr)
    currMax = arr[0]
    currMin = arr[0]
    prod = arr[0]
    for i in range (1,n):
        temp = max(arr[i],currMax*arr[i],currMin*arr[i])
        currMin = min(arr[i],currMax*arr[i],currMin*arr[i])
        currMax = temp
        prod = max(prod,currMax)
    return prod

arr = [-2,6,-3,-10,0,2]
print(maxProduct(arr))
# Time Complexity: O(n)
# Space Complexity: O(1)
# This code implements a solution to find the maximum product of a contiguous subarray.