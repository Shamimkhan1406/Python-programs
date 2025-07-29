
"""
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Four triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
"""
def findTriplet(arr, k):
    res = 0
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum > k:
                right -= 1
            elif sum < k:
                left += 1
            else:
                ele1 = arr[left]
                ele2 = arr[right]
                cnt1 = 0
                cnt2 = 0
                while left <= right and arr[left] == ele1:
                    cnt1 += 1
                    left += 1
                while left <= right and arr[right] == ele2:
                    cnt2 += 1
                    right -= 1
                if ele1 == ele2:
                    res += (cnt1 * (cnt1 -1))//2
                else:
                    res += cnt1 * cnt2
    return res
if __name__ == "__main__":
    arr = [-17, -16, -12, -9, -4, -4, -2, 13, 16]
    k = 0
    print(findTriplet(arr, k)) #4

# Time Complexity: O(n^2)
# Space Complexity: O(1) since we are using only a few variables for counting and indexing.
# The algorithm uses a two-pointer technique to find pairs that, along with the current element, sum up to the target value.