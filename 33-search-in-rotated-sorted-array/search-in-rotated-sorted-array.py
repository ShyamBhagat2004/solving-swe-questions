class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L+R)//2
            if target == nums[M]:
                return M
            if nums[L] <= nums[M]:

                if nums[L] <= target < nums[M]:
                    #in middle of sorted left array
                    R = M-1
                else:
                    L = M+1
            else:
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1


        return -1