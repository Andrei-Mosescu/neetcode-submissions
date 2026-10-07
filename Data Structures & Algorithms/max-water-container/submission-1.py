class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi, i, j = 0, 0, len(heights)-1
        while i<j:
            h = heights[i] - heights[j]
            if h > 0:
                maxi = max(maxi, heights[j]*(j-i))
                j -= 1
            else:
                maxi = max(maxi, heights[i]*(j-i))
                i += 1
        
        return maxi