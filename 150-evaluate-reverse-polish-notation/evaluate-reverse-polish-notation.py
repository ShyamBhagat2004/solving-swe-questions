import operator
import operator

class Solution:

    #This is the solution I came up with myself, below is the optimized solution
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []



        for val in tokens:

            if val.lstrip('-').isdigit():
                val = int(val)
                stack.append(val)
            else:

                    #for each operation
                if val == '+':
                    hold = stack.pop()
                    hold2 = stack.pop()                  
                    stack.append(hold2+hold)
                if val == '-':
                    hold = stack.pop()
                    hold2 = stack.pop()                  
                    stack.append(hold2-hold)
                if val == '*':
                    hold = stack.pop()
                    hold2 = stack.pop()                  
                    stack.append(hold*hold2)
                if val == '/':
                    hold = stack.pop()
                    hold2 = stack.pop()                  
                    stack.append(int(hold2/hold))
     

        return int((stack[-1]))



    def evalRPN2(self, tokens: List[str]) -> int:

        stack = []

        ops = {

            '+': operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }

        for token in tokens:

            if token not in ops:
                stack.append(int(token))
            else:

                n2 = stack.pop()
                n1 = stack.pop()
                res =  ops[token](n1, n2)
                stack.append(int(res))
        return stack[-1]





       

            

            

        
        


        




       

            

            

        
        


        
