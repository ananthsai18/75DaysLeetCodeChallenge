class Solution:
    def isValid(self, s: str) -> bool:
        valid={')':'(','}':"{","]":"["}
        stack=[]
        for i in s:
            if i not in valid:
                stack.append(i)
            elif (stack and stack[-1]==valid[i]):
                stack.pop()
            else:
                return False
        if len(stack)!=0:
            return False
        return True