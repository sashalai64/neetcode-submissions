class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s:
            freq1[ord(c) - ord('a')] += 1
        
        for c in t:
            freq2[ord(c) - ord('a')] += 1
        
        return freq1 == freq2