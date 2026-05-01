class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            t, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            
            visited.add(cur)
            res = t

            for neigh, time in graph[cur]:
                if neigh not in visited:
                    heapq.heappush(heap, (t + time, neigh))
            
        return res if len(visited) == n else -1