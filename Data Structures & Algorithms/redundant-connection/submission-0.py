class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            cur = q.popleft()
            
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                indegree[cur] -= 1
                if indegree[neigh] == 1:
                    q.append(neigh)

        for u, v in edges[::-1]:
            if indegree[u] >= 2 and indegree[v] >= 2:
                return [u, v]

        return []
            