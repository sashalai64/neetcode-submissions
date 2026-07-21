class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []

        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1

            dic[tuple(temp)].append(s)
        
        return list(dic.values())
        
