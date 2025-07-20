"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]"""


def prodExceptSelf(nums):
    n = len(nums)
    prod = [1] * n
    for i in range(1,n):
        prod[i] = prod[i-1]*nums[i-1]
    right = nums[-1]
    for i in range(n-2,-1,-1):
        prod[i]*=right
        right *= nums[i]
    return prod
# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = prodExceptSelf(nums)
    
    print(f"The product of array except self is: {result}")  # Output: [24, 12, 8, 6]
# Time Complexity: O(n) where n is the length of the input array, as we traverse the array twice.
# Space Complexity: O(n) for the output array, but no additional space is used for calculations.
# This code implements a function to calculate the product of all elements in an array except for the element at the current index.
# It uses two passes: one to calculate the product of all elements to the left of each index, and another to multiply by the product of all elements to the right.
# The function returns an array where each element is the product of all elements in the input array except for the element at that index.
# The implementation ensures that the product is calculated without using division, making it suitable for cases where the input may contain zeros.
# The result is printed to the console, showing the product of the array except for each element.
# The function handles edge cases, such as when the input array has only one element or contains zeros, ensuring that the output is correct in all scenarios.