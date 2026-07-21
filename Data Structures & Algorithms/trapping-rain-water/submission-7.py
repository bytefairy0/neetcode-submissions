class Solution:
    def trap(self, height: List[int]) -> int:
        # key was to find area above each bar :((
        
        n = len(height)
        
        leftMax = [height[0]]
        rightMax = [0] * n
        rightMax[-1] = height[-1]

        for i in range(1, n):
            if leftMax[-1] < height[i]:
                leftMax.append(height[i])
            else:
                leftMax.append(leftMax[-1])
            # build rightMax array from reverse
            if rightMax[n-i] < height[n-1-i]:
                rightMax[n-1-i] = height[n-1-i]
            else: 
                rightMax[n-1-i] = rightMax[n-i]

        totalArea = 0
        for i in range(n):
            area = min(leftMax[i], rightMax[i]) - height[i]
            totalArea += area
        
        return totalArea


        