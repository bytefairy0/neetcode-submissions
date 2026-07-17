class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p1, p2 = 0, n-1
        areaMax = 0
        while p1<p2:
            h1, h2 = heights[p1], heights[p2]
            area = (p2-p1)*(min(h1, h2))
            if area > areaMax:
                areaMax = area
            
            # move ptr with smaller height
            if h1 < h2:
                p1 += 1
            else:
                p2 -= 1

        return areaMax
