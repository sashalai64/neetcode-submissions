class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        prev = 0
        res = 0

        for p, s in cars:
            time = (target - p) / float(s)
            if not prev or time > prev:
                res += 1
                prev = time
        
        return res