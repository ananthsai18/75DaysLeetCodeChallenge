class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in s:
            if s1 and i=='#':
                s1.pop()
            elif i=="#":
                continue
            else:
                s1.append(i)
        for i in t:
            if s2 and i=='#':
                s2.pop()
            elif i=="#":
                continue
            else:
                s2.append(i)
        print(s1,"___",s2)
        if "".join(s1)=="".join(s2):
            return True
        return False

        