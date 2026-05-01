class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, cur):
            if left == right == n:
                res.append(cur[:])
                return
            
            if left < n:
                dfs(left + 1, right, cur + '(')
            if right < left:
                dfs(left, right + 1, cur + ')')
            

        res = []
        dfs(0, 0, '')

        return res