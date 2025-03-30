class solution:
    def reverseArray(arr):
        n = len(arr)
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return arr
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", solution.reverseArray(arr))