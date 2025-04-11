class solution:
    def rotateArray(arr,d):
        n= len(arr)
        d=d%n
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)
def reverse(arr,low,high):
    while low<high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
print("Original array:", arr)
solution.rotateArray(arr,d)
print("Rotated array:", arr)
# Time Complexity: O(n)
# Space Complexity: O(1)
# The function rotates the array in place, so it does not require any extra space.