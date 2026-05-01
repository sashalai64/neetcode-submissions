class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        freq = defaultdict(int)

        for c in t:
            if c not in count or count[c] == 0:
                return False
            freq[c] += 1
        
        return count == freq