class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_e = intervals[0][1]
        res = 0

        for s, e in intervals[1:]:
            if s >= prev_e:
                prev_e = e
            else:
                res += 1
                prev_e = min(prev_e, e)
        
        return res