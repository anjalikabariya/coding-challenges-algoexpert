'''Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals,
and returns the new intervals in no particular order.
Each interval interval is an array of two integers, with interval[0] as the start of the interval and
interval[1] as the end of the interval.
Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7]
aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.
Also note that the start of any particular interval will always be less than or equal to the end of that interval.

Sample Input
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Sample Output
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.
'''

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    # sort intervals based on first value
    # compare each interval starting from 2nd position with it's previous interval
    # compare starting value of current interval with ending value of previous interval
    # if overlapping, merge intervals and assign last value as max of both interval's last value
    # if not overlapping move to next interval
    intervals.sort(key=lambda x: x[0])
    index = 0
    for i in range(1, len(intervals)):
        if (intervals[index][1] >= intervals[i][0]):
            intervals[index][1] = max(intervals[i][1], intervals[index][1])
        else:
            index += 1
            intervals[index] = intervals[i]
    intervals = intervals[:index+1]
    return intervals
    # print(intervals)
