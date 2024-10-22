class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L, R = 0, len(nums)-1
        while L <= R:
            M = (L+R)//2
            if L == R:
                return nums[M]
            if nums[M] > nums[R]:
                #We are in the left part of the array that is sorted
                L = M + 1
            else:
                R = M
        


            



        

        

        