class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxLen = 0
        l = 0
        res = 0
         
        # loop thru s
        for r in range(len(s)):
            freq[s[r]] += 1
            # get the most frequent char count
            maxLen = max(maxLen, freq[s[r]])
    
            # check if the replacement > k (r - l + 1 - maxLen > k)
            while r - l + 1 - maxLen > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res