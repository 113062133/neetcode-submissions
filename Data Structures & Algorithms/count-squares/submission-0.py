class CountSquares:

    def __init__(self):
        self.m = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        if p in self.m:
            self.m[p] += 1
        else:
            self.m[p] = 1

    def count(self, point: List[int]) -> int:
        qx = point[0]
        qy = point[1]
        res = 0

        for p in self.m:
            x = p[0]
            y = p[1]
            if abs(x - qx) == abs(y - qy) and x != qx:
                if (x, y) in self.m and (x, qy) in self.m and (qx, y) in self.m:
                    res += self.m[(x, y)] * self.m[(x, qy)] * self.m[(qx, y)]
        return res
