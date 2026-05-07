class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        if len(position) == 0:
            return 0
        for i in range(len(position)):
            car.append((position[i], speed[i]))
        car.sort(reverse=True)
        leadingCount = 0
        longesttime = 0
        for pos, speed in car:
            time = (target - pos) / speed
            if time > longesttime:
                leadingCount += 1
                longesttime = time
        return leadingCount
            



        