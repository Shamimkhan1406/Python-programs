class Solution:
    
    def check(self, arr,k,limit):
        count = 1
        sum=0
        for pages in arr:
            if pages+sum>limit:
                count += 1
                sum = pages
            else:
                sum += pages
        return count<=k
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if k>len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        res = -1
        while low <= high:
            mid = low+(high-low)//2
            if self.check(arr,k,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res

# problem: Allocate minimum number of pages to k students such that maximum number of pages allocated to a student is minimum.
# given an array of integers where each integer represents the number of pages in a book, and an integer k representing the number of students.
# the task is to allocate books to students such that the maximum number of pages allocated to a student is minimized.
# the function returns the minimum number of pages that can be allocated to a student
# the function uses binary search to find the minimum number of pages that can be allocated to a student
# the function checks if it is possible to allocate books to k students such that the maximum number of pages allocated to a student is less than or equal to a given limit
# the function returns the minimum number of pages that can be allocated to a student
# time complexity: O(nlog(sum(arr)))
# space complexity: O(1)