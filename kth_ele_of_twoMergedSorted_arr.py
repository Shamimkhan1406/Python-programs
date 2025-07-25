def findKthElement(arr1,arr2, k):
    n,m = len(arr1),len(arr2)
    i , j = 0, 0
    kth = 0
    for _ in range(k):
        if i < n:
            if j<m and arr1[i]>arr2[j]:
                kth = arr1[j]
                j+=1
            else:
                kth = arr1[i]
                i+=1
        elif j<m:
            kth = arr2[j]
            j+=1
    return kth

# Example usage
if __name__ == "__main__":
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k = 5
    result = findKthElement(arr1, arr2, k)
    
    print(f"The {k}th element in the merged sorted array is: {result}")  # Output: 6
# Time Complexity: O(k) where k is the index of the element we want to find
# Space Complexity: O(1) as we are using a constant amount of space.
# This code implements a function to find the kth element in the merged sorted array of two sorted arrays.
# It iterates through both arrays, comparing elements and keeping track of the kth element.
# The function handles cases where one array is exhausted before the other, ensuring that it continues to find the kth element correctly.
# The result is printed to the console, showing the kth element in the merged sorted array.
# The function ensures that the search is efficient and suitable for applications where finding specific elements in merged sorted data is required.
# The implementation is straightforward and handles edge cases, such as when k is larger than the total number of elements in the merged array.
# The result is printed to the console, showing the kth element in the merged sorted array.