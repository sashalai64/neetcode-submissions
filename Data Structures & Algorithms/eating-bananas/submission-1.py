class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatTime(speed):
            total = 0
            for p in piles:
                total += math.ceil(p / speed)
            return total

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = eatTime(mid)

            # last values <= h
            if time <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l