
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        myList = []

        for key in range(len(nums)):
            if key > 0 and nums[key] == nums[key - 1]:
                continue
            L, R = key + 1, len(nums) - 1
            while L < R:
                mySum = nums[key] + nums[L] + nums[R]
                if mySum > 0:
                    R -= 1
                elif mySum < 0:
                    L += 1
                else:
                    myList.append([nums[key], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                         L += 1
                    while L < R and nums[R] == nums[R - 1]:
                         R -= 1
                    L += 1
                    R -= 1

        return myList
