class Solution:
    def numDecodings(self, s: str) -> int:
        def backtrack(i):
            nonlocal res

            if i >= n:
                res += 1
                return

            if s[i] == '0':
                return

            backtrack(i + 1)

            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                backtrack(i + 2)

        n = len(s)
        res = 0
        backtrack(0)

        return res