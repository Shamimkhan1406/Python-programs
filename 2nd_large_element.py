class solution:
    def secondLarge(arr):
        n = len(arr)
        if n<2:
            return -1
        first = second = -1
        for i in range(n):
            if arr[i] > first:
                second = first
                first = arr[i]
            elif arr[i] > second and arr[i] < first:
                second = arr[i]
        return second
    
arr = [12, 35, 1, 10, 34, 1]
print("The second largest element is", solution.secondLarge(arr))
# Output: The second largest element is 34