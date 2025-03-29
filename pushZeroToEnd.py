class pushZeroToEnd:
    def push_zero_end(arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i],arr[count] = arr[count],arr[i]
                count += 1
        return arr
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print("Array after pushing zeros to the end:", pushZeroToEnd.push_zero_end(arr))