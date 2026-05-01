class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for c in s:
            hashmap1[c] += 1
        for c in t:
            hashmap2[c] += 1
        
        return hashmap1 == hashmap2
        