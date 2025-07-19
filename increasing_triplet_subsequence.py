"""Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""
class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
#Example:
if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    sol = Solution()
    print(sol.increasingTriplet(nums))  # Output: True
    nums = [5, 4, 3, 2, 1]
    print(sol.increasingTriplet(nums))  # Output: False
    nums = [1, 2, 3, 4, 5]
    print(sol.increasingTriplet(nums))  # Output: True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sol.increasingTriplet(nums))  # Output: True
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(sol.increasingTriplet(nums))  # Output: False

# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using only a few extra variables.
# This code implements a linear time solution to check if there exists an increasing triplet subsequence
# in the given array. It uses two variables to keep track of the first and second smallest elements seen so far.
# If a third element is found that is greater than the second, it indicates that an increasing triplet subsequence exists.
# If no such triplet is found, it returns false.
# The algorithm iterates through the array only once, making it efficient for large inputs.
# The solution is optimal and does not require any additional data structures, thus maintaining a constant space complexity.
# The approach is based on the observation that if we can find two elements such that the first is less than the second,
# and a third element that is greater than the second, then we have found our increasing triplet subsequence.
# The algorithm efficiently updates the first and second smallest elements as it traverses the array,
# ensuring that we always have the smallest possible values for comparison.

    