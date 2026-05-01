class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        visited = set()
        res = 0

        while heap:
            dis, cur = heapq.heappop(heap)
            if cur in visited:
                continue
                
            visited.add(cur)
            res += dis

            for i in range(n):
                new = abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1])
                heapq.heappush(heap, (new, i))

        return res