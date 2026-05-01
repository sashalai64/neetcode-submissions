class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        l, k, r = 0, 0, n - 1

        for l in range(n - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            k = l + 1
            r = n - 1
            while k < r:
                total = nums[l] + nums[k] + nums[r]

                if total == 0:
                    res.add((nums[l], nums[k], nums[r]))
                    k += 1
                    r -= 1
                
                elif total > 0:
                    r -= 1
                
                else:
                    k += 1

        
        return list(res)