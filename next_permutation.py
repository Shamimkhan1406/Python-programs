class solution:
    def nextPermutation(arr):
        n = len(arr)
        pivot = -1
        #find pivot element which is the first element from the right which is smaller than its next element
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot = i
                break
        #if pivot is -1 then the array is in descending order and we need to reverse the array
        if pivot == -1:
            arr.reverse()
            return arr
        #find the rightmost element which is greater than pivot
        for i in range(n-1,pivot,-1):
            if arr[i]>arr[pivot]:
                #swap the pivot and the rightmost element
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break
        #reverse the element from the pivot+1 to the end of the array
        left = pivot+1
        right = n-1
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
        return arr
arr = [1, 2, 3]
print("Original array:", arr)
print("Next permutation:", solution.nextPermutation(arr))
# Time Complexity: O(n)
# Space Complexity: O(1)
# The function modifies the array in place, so it does not require any extra space.
