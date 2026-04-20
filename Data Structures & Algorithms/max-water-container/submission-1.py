class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = - 1
        for i in range(len(heights)):
            for j in range (i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxA = max(area, maxA)
        
        return maxA
        