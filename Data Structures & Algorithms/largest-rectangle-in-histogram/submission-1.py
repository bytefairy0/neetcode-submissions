class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            width = 1
            # area from backward
            k = i-1
            while k>=0 and heights[i] <= heights[k]:
                width += 1 
                k -= 1
            # area from forward
            l = i+1
            while l<n and heights[i] <= heights[l]:
                width += 1
                l += 1
            area = width*heights[i]
            if area > maxArea:
                maxArea = area

        return maxArea

        