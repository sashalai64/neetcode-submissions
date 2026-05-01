class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        q.append((src, 0))
        visited = [float('inf')] * n
        flightMap = defaultdict(list)

        for s, e, d in flights:
            flightMap[s].append((e, d))
        
        while q and k >= 0:
            for _ in range(len(q)):
                cur, cur_price = q.popleft()
                for neigh, neigh_price in flightMap[cur]:
                    new_price = cur_price + neigh_price
                    if new_price < visited[neigh]:
                        visited[neigh] = new_price
                        q.append((neigh, new_price))
            k -= 1
        
        return visited[dst] if visited[dst] != float('inf') else -1