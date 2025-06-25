class solution:
    def bruteForce(self, arr):
        res = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    res += 1
        return res
        # Time Complexity: O(n^2), where n is the number of elements in the array.
        # Space Complexity: O(1), as we are using only a few extra variables.
        # This code implements a brute force method to count the number of inversions in an array.
        # An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].

    def mergeSort(self, arr,start,end):
        res = 0
        if start < end:
            mid = (start + end)//2
            res+=self.mergeSort(arr,start,mid)
            res+=self.mergeSort(arr,mid+1,end)
            res+=self.merge(arr,start,mid,end)
        return res
    def merge(self, arr, start, mid, end):
        res = 0
        n1 = mid - start + 1
        n2 = end - mid
        # Create temporary arrays
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = 0
        j = 0
        k = start
        # Merge the temporary arrays
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                res += (n1 - i)
                j += 1
            k += 1
        # Copy the remaining elements of left, if any
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        # Copy the remaining elements of right, if any
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        # Return the count of inversions 
        return res

    def countInversions(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)
if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    sol = solution()
    inversion_count = sol.countInversions(arr)
    print("Number of inversions are", inversion_count)
    print("Sorted array is", arr)
# Time Complexity: O(n log n), where n is the number of elements in the array.
# Space Complexity: O(n), due to the temporary array used for merging.
# This code implements a modified merge sort algorithm to count the number of inversions in an array.
# An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
# The algorithm counts inversions while merging two sorted subarrays.
# The merge function combines two sorted subarrays and counts the inversions by checking how many elements in the left subarray are greater than elements in the right subarray.
# The total number of inversions is returned after sorting the array.