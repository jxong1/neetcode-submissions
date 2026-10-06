class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largest = 0
        hStack = []
        for i, height in enumerate(heights):
            diff = 0
            while hStack and height < heights[hStack[-1][0]]:
                largest = max(largest, heights[hStack[-1][0]] * (i - hStack[-1][0] + hStack[-1][1]))
                diff += hStack.pop()[1]
                diff += 1
            hStack.append((i, diff))
        for i, diff in hStack:
            largest = max(largest, (len(heights) - i + diff) * heights[i])
        return largest