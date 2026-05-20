class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stackMax = [[heights[0],0]]
        maxArea = heights[0]

        for index , height in enumerate(heights) :
            maxArea = max(maxArea , height)
            
            for hgt , i in stackMax :
                    maxArea = max(maxArea,min(hgt,height) * (index - i + 1))

            if height > stackMax[-1][0] or index == len(heights)-1:
                stackMax.append([height,index])

            for i in range(len(stackMax)):
                stackMax[i][0] = min(stackMax[i][0], height)

        
        
        return maxArea
