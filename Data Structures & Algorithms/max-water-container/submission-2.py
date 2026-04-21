class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = -1
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxA = max(area, maxA)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA

    
        """
        maxA = - 1
        for i in range(len(heights)):
            for j in range (i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxA = max(area, maxA)
        
        return maxA
        """
        