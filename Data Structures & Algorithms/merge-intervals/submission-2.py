class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        i = 1
        intervals.sort()
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1] = [min(intervals[i-1][0], intervals[i][1]), max(intervals[i-1][1], intervals[i][1])]
                del(intervals[i])
            else:
                i += 1
        return intervals