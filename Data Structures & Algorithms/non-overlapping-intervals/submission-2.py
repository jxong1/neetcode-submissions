class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1] or (i + 1 < len(intervals) and intervals[i+1][0] < intervals[i][1]):
                if intervals[i][0] < intervals[i-1][1] and (i + 1 < len(intervals) and intervals[i+1][0] < intervals[i][1]):
                    del(intervals[i])
                    removed += 1
                elif (i + 1 < len(intervals) and intervals[i+1][0] < intervals[i][1]):
                    i += 1
                else:
                    del(intervals[i-1])
                    removed += 1
            else:
                i += 1
        return removed
