class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)

        curtime=0
        fleets=0

        for position , speed in cars:
            time=(target-position)/speed
            if time > curtime:
                fleets+=1
                curtime=time
        return fleets 