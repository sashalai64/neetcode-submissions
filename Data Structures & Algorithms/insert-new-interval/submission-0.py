class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]

        for s, e in intervals[1:]:
            if s <= res[-1][1]:
                prev_s, prev_e = res.pop()
                res.append([min(s, prev_s), max(e, prev_e)])
            else:
                res.append([s, e])
        
        return res