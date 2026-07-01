class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cell = list(zip(position, speed))
        cell.sort(reverse=True)
        stack = []

        for i in range(len(cell)):
            time = (target - cell[i][0]) / cell[i][1]
            if i == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)
