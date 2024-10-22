class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height)-1

        res = 0
        while l<r:

            prod = min(height[l], height[r]) * (r-l)
            if prod > res:
                res = prod
            
            if height[l] < height[r]:
                l +=1
            elif height[r] <= height[l]:
                r -=1
            
        return res

        