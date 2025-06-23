
def sort012(arr):
    n = len(arr)
    low = 0
    mid =0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high],arr[mid]
            high -= 1
    return arr
# Example usage
arr = [0, 1, 2, 0, 1, 2, 1, 0]
sorted_arr = sort012(arr)
print(sorted_arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2]
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), as we are sorting the array in place.
# This code implements the Dutch National Flag problem to sort an array containing only 0s, 1s, and 2s.
# It uses three pointers: low, mid, and high to partition the array into three sections.
# The low pointer tracks the position for 0s, mid tracks the current element being processed, and high tracks the position for 2s.
# The algorithm iterates through the array, swapping elements as needed to ensure that all 0s are at the beginning,
# all 1s are in the middle, and all 2s are at the end.
# This approach is efficient and works in linear time, making it suitable for sorting arrays with a limited range of values.
# The function returns the sorted array.