class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = 0, 0
        res = 0

        while l <= r:
            if lMax < rMax:
                if lMax - height[l] > 0:
                    res += lMax - height[l]
                lMax = max(height[l], lMax)
                l += 1
            else:
                if rMax - height[r] > 0:
                    res += rMax - height[r]
                rMax = max(height[r], rMax)
                r -= 1
        
        return res