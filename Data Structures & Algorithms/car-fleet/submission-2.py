class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        prev = (target - pair[0][0]) / pair[0][1]

        for i in range(len(position)):
            time = (target - pair[i][0]) / pair[i][1]
            if time > prev:
                res += 1
                prev = time
        
        return res