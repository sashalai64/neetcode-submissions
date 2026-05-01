class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()

        for i in range(n):
            hashmap = defaultdict(int)
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                if -total in hashmap:
                    res.add((nums[i], nums[hashmap[-total]], nums[j]))
                hashmap[nums[j]] = j
        
        return list(res)