class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, cur):
            if l == r == n:
                res.append(cur)
                return
            
            if l < n:
                dfs(l + 1, r, cur + '(')

            if r < l:
                dfs(l, r + 1, cur + ')')

        res = []
        dfs(0, 0, '')

        return res