class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list) # {node: [node1, node2]}

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        q = deque() # (node, parent)
        visited = set()
        q.append((0, -1))

        while q:
            node, parent = q.popleft()
            n -= 1

            for neigh in graph[node]:
                if neigh == parent:
                    continue
                
                if neigh in visited:
                    return False
                
                visited.add(neigh)
                q.append((neigh, node))
        
        return n == 0