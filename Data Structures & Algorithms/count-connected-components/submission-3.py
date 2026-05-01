class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        res = 0
        seen = set()

        for start in range(n):
            if start in seen:
                continue
            
            res += 1
            q = deque()
            q.append(start)
            visited = set()
            visited.add(start)
            seen.add(start)

            while q:
                cur = q.popleft()
    
                for neigh in graph[cur]:
                    if neigh in visited:
                        continue
                    
                    q.append(neigh)
                    visited.add(neigh)
                    seen.add(neigh)
        
        return res if res <= n else n





