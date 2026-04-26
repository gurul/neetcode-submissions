class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append((position[i], speed[i]))

        stack.sort(key=lambda x: x[0])

        fleets = 0

        while stack:
            curr = stack.pop()
            time = (target - curr[0]) / curr[1]

            while stack and (target - stack[-1][0]) / stack[-1][1] <= time: 
                stack.pop()

            fleets += 1

        return fleets





        