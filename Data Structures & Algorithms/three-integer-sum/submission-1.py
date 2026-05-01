class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        
        for l in range(n-2):
            hashmap = defaultdict(int)
            target = -nums[l]
            
            for r in range(l+1, n):
                diff = target - nums[r]
                if diff in hashmap:
                    res.add((nums[l], nums[hashmap[diff]], nums[r]))
                else:
                    hashmap[nums[r]] = r
        
        return list(res)