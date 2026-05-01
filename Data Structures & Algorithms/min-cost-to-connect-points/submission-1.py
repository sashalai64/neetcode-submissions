class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)]
        visited = set()
        res = 0
        cache = {0: 0}
        
        while minHeap:
            cost, u = heapq.heappop(minHeap)
            if u in visited:
                continue

            visited.add(u)
            res += cost

            for v in range(len(points)):
                dis = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dis < cache.get(v, float('inf')):
                    cache[v] = dis
                    heapq.heappush(minHeap, (dis, v))

        return res