class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myDict = {}

        for key, val in enumerate(nums):
            if target-val in myDict:
                return key, myDict[target-val]
            else:
                myDict[val] = key   
            


        

