class solution:
    def searchKeyElement(self,arr,key):
        n = len(arr)
        low =0
        high = n-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] == key:
                return mid
            if arr[low] <= arr[mid]: # Left half is sorted
                if arr[low] <= key < arr[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else: # Right half is sorted
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1
# Example usage
if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2]
    key = 0
    sol = solution()
    index = sol.searchKeyElement(arr,key)
    
    if index != -1:
        print(f"The key element {key} is found at index {index}")
    else:
        print(f"The key element {key} is not found in the array")
# Time Complexity: O(log n) as we are using binary search.
# Space Complexity: O(1) as we are using a constant amount of space.
# This code implements a function to search for a key element in a rotated sorted array.
# It uses binary search to efficiently locate the key element by checking which half of the array is sorted.
# The function iteratively narrows down the search range based on the properties of the rotated sorted array.
# If the key element is found, its index is returned; otherwise, -1 is returned to indicate that the key is not present in the array.
# The example usage demonstrates how to call the function and print the result.
# The function ensures that the search is efficient and suitable for large arrays, making it a common approach in problems involving rotated sorted arrays.
# The implementation handles edge cases, such as when the array has only one element or when the key is at the boundaries.
# The result is printed to the console, showing the index of the key element if found, or a message indicating that the key is not present in the array.