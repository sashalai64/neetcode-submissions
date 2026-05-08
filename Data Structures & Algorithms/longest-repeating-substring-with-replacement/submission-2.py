class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxLen = 0
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            maxLen = max(maxLen, freq[s[r]])
            
            while r - l + 1 - maxLen > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
