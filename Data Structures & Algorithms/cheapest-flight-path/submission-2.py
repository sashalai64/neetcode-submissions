class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, dest, price in flights:
            graph[s].append((dest, price))
        
        q = deque([(0, src, 0)])
        prices = [float('inf')] * n
        prices[src] = 0

        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                break

            for nei, w in graph[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float('inf') else -1 