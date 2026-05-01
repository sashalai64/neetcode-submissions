"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0

        intervals.sort(key = lambda x: x.start)
        heap = []

        for intervals in intervals:
            if heap and intervals.start >= heap[0][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, [intervals.end, intervals.start])

        return len(heap)
        