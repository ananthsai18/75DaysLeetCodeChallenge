class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack1=[]
        n=len(operations)
        for i in range(n):
            if operations[i]=='+':
                a=stack1.pop()
                b=stack1.pop()
                stack1.append(b)
                stack1.append(a)
                stack1.append(a+b)
            elif operations[i]=='C':
                stack1.pop()
            elif operations[i]=='D':
                a=stack1.pop()
                stack1.append(a)
                stack1.append(a*2)
            else:
                stack1.append(int(operations[i]))
                
        return sum(stack1)

            


        