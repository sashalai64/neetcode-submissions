class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)

        n = len(nums)
        k = n - k
        return quickSelect(0, len(nums) - 1)