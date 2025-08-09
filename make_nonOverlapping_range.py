def minRemoval(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0]<end:
            count += 1
        else:
            end = intervals[i][1]
    return count

# Example usage:
if __name__ == "__main__":
    intervals = [[1, 3], [2, 4], [3, 5], [6, 8]]
    removals = minRemoval(intervals)
    print("Minimum Removals:", removals)  # Output: Minimum Removals: 1
# Time Complexity: O(n log n), where n is the number of intervals, due to sorting.
# Space Complexity: O(1), as we are using only a few extra variables.
# This code implements a function to find the minimum number of intervals to remove so that the remaining intervals do not overlap.
# It sorts the intervals based on their end times and iterates through them to count how many intervals overlap with the current end time.
# The function keeps track of the end time of the last added interval and increments the count whenever it finds an overlapping interval.
# The final count gives the minimum number of intervals that need to be removed to achieve non-overlapping intervals.
# The function returns the count of intervals that need to be removed, which can be used for further processing or output.
# The function ensures that the remaining intervals are non-overlapping by always considering the earliest ending interval first.
# This greedy approach is efficient and works well for this problem.