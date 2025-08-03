def mergeOverlap(arr):
    res = []
    arr.sort()
    res.append(arr[0])
    for i in range(1,len(arr)):
        curr = arr[i]
        last = res[-1]
        if last[1] >= curr[0]:
            last[1] = max(last[1],curr[1])
        else:
            res.append(curr)
    return res

# Example usage:
if __name__ == "__main__":
    intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
    merged_intervals = mergeOverlap(intervals)
    print("Merged Intervals:", merged_intervals)
# Time Complexity: O(n log n), where n is the number of intervals, due to sorting.
# Space Complexity: O(n), for storing the merged intervals.
# This code implements a function to merge overlapping intervals.
# It first sorts the intervals based on their start times, then iterates through them to merge any overlapping intervals.
# The result is a list of merged intervals, ensuring that no two intervals overlap.
# The function handles cases where intervals are completely overlapping or partially overlapping.
# The merged intervals are returned in a list, which can be used for further processing or output.
