class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append((0, -1)) # [(node, parent)]
        visited = set({0})

        while q:
            cur, parent = q.popleft()
            
            for neigh in adj[cur]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                
                q.append((neigh, cur))
                visited.add(neigh)

        return len(visited) == n


        '''
        1. no cycles -> if len(visited) == n
        2. fully connected -> track parent


        0 - 1 - 2
             \ /
              3

        '''