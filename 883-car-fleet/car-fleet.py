class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        res = []
        for i, j in zip(position, speed):
            pair.append([i, j])
        
        for pos, speed in sorted(pair)[::-1]:
            res.append((target-pos)/speed)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)