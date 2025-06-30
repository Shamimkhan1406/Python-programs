def insertionSort(arr):
    for i in range(1,len(arr)):
        j= i
        while arr[j-1]>arr[j]and j>0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertionSort(arr)
    print("Sorted array:", sorted_arr)
# Time Complexity: O(n^2), where n is the number of elements in the array.
# Space Complexity: O(1), as we are sorting the array in place.
# This code implements the insertion sort algorithm, which builds a sorted array one element at a time.
# It iterates through the array, and for each element, it finds the correct position in the already sorted part of the array and inserts it there.
# The algorithm is efficient for small datasets and is a stable sort, meaning that it maintains the relative order of equal elements.
# The insertion sort algorithm is particularly useful for nearly sorted arrays and small datasets.
# It is also used as a subroutine in more complex algorithms like merge sort and quicksort for small arrays.