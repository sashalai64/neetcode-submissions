class Solution:
    def numDecodings(self, s: str) -> int:
        def backtrack(i):
            if i in memo:
                return memo[i]

            if i >= n:
                return 1
                
            if s[i] == '0':
                return 0

            res = backtrack(i + 1)

            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += backtrack(i + 2)
            
            memo[i] = res
            return res

        n = len(s)
        memo = {}
        return backtrack(0)