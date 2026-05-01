class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ''

        while i < len(strs[0]):
            for s in strs:
                c = strs[0][i]
                if i >= len(s) or s[i] != c:
                    return res
            res += c
            i += 1
        
        return res