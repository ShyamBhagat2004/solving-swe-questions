class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        myDict = {
            '(':')',
            '[':']',
            '{':'}'}

        myDict = dict((v,k) for k,v in myDict.items())
            



        
        for c in s:

            if c in "({[":
                
                myStack.append(c)
            else:
                if myStack:
                    if myDict[c] == myStack[-1]:
                        myStack.pop()
                    else:
                        return False
                else:
                    return False
                    
                
        return len(myStack) == 0

                
            
        