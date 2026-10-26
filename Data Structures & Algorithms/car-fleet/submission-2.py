class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        ttd_fleet = 0
        for p, s in sorted(zip(position, speed), reverse=True):
            ttd = (target-p)/s
            if ttd > ttd_fleet:
                fleets += 1
                ttd_fleet = ttd
            
        return fleets
                