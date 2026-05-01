class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)

            if (i + 1 < n) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                res += dfs(i + 2)

            cache[i] = res
            return res

        n = len(s)
        return dfs(0)
        