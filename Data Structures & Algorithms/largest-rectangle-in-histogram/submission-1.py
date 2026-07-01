class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for right in range(0, n + 1):
            height = 0 if right == n else heights[right]
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = right if not stack else right - stack[-1] - 1
                area = h * width
                max_area = max(area, max_area)
            stack.append(right)
        return max_area