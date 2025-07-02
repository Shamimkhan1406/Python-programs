class solution:

    def mergeSort(self, arr,start,end):
        if start < end:
            mid = (start + end)//2
            self.mergeSort(arr,start,mid)
            self.mergeSort(arr,mid+1,end)
            self.merge(arr,start,mid,end)
    def merge(self, arr, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= end:
            temp.append(arr[j])
            j += 1
        for i in range(len(temp)):
            arr[i + start] = temp[i]
# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sol = solution()
    sol.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
# Time Complexity: O(n log n), where n is the number of elements in the array.
# Space Complexity: O(n), due to the temporary array used for merging.
# This code implements the merge sort algorithm, which is a divide-and-conquer sorting algorithm.
# It recursively divides the array into halves, sorts each half, and then merges the sorted halves.
# The merge function combines two sorted subarrays into a single sorted array.
# The algorithm is efficient for large datasets and guarantees a stable sort.
# The merge sort algorithm is particularly useful for sorting linked lists and large datasets that do not fit into memory.
    
