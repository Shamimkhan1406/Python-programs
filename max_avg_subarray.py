"""
ou are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        currSum = maxSum = sum(nums[:k])
        j = 0
        for i in range(n-k):
            currSum += nums[i+k]-nums[i]
            maxSum = max(maxSum,currSum)
        return float(maxSum)/k

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1,2,3,4,5], 2)) # 4.5
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75

# Time complexity: O(n)
# Space complexity: O(1) as we are using constant space for variables.