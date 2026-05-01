class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp1 = [0] * n # rob first
        dp2 = [0] * n # rob last

        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[1] = nums[1]

        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        
        return max(dp1[-2], dp2[-1])
