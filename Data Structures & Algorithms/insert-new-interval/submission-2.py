class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                del(intervals[i])
            elif interval[0] > newInterval[1]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                return intervals
            else:
                i += 1
        intervals.append(newInterval)
        return intervals