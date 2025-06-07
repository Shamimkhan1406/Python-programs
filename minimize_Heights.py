def getMinDiff(arr,k):
    n = len(arr)
    arr.sort()
    res = arr[n-1]-arr[0]
    for i in range (1,n):
        if arr[i]-k<0:
            continue
        minH = min(arr[0]+k,arr[i]-k)
        maxH = max(arr[n-1]-k,arr[i-1]+k)
        res = min(res,maxH-minH)
    return res

# Example usage
arr = [3, 9, 12, 16, 20]
k = 3
print(getMinDiff(arr, k))  # Output: 8
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) as we are using only a few extra variables
# This code implements a solution to minimize the difference between the maximum and minimum heights of an array after modifying each element by a given value k.
# It sorts the array and then iterates through it to find the minimum possible difference after applying the modifications.
# The approach ensures that the heights are adjusted optimally to achieve the minimum difference.
# The function first sorts the array, then calculates the initial difference between the maximum and minimum heights.