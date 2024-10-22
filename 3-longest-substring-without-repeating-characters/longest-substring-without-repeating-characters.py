class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #contiguous set of numbers

        #sliding window approach

        maxCount = 0
        L, R = 0,0
        mySet = set()
        count = 0
        while R < len(s):

            if s[R] not in mySet:
                mySet.add(s[R])
                count += 1
                R += 1
                maxCount = max(maxCount, count)
                
            else:
                maxCount = max(maxCount, count)
                L += 1
                R = L
                count = 0
                mySet.clear()
            
        return maxCount
                
















        


      