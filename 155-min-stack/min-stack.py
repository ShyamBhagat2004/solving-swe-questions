class MinStack:

    def __init__(self):

        self.stack = []
        self.mStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.mStack:
            self.mStack.append(min(val, self.mStack[-1]))
        else:
            self.mStack.append(val)
    
        
    def pop(self) -> None:

        if self.stack:
            self.stack.pop()
            self.mStack.pop()
        else:
            pass
        
    def top(self) -> int:

        if self.stack:

            return self.stack[-1]
        else:
            return -1
        

    def getMin(self) -> int:

        if self.mStack:
            return self.mStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()