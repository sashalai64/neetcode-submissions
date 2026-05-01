class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)] # parent is itself
        rank = [1] * (n + 1)

        # find root parent
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
           
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # if n1, n2 are connected
            if p1 == p2:
                return False
            
            # p2 be the child of p1
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]