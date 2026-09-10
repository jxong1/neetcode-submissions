class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, spd] for pos, spd in zip(position, speed)]
        cars.sort()
        times = []

        for i in range(len(cars) - 1, -1, -1):
            pos, spd = cars[i]
            time = (target - pos) / spd
            if not times or time > times[-1]:
                times.append(time)
        return len(times)