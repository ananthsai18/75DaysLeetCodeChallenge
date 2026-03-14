class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t_count={}
        s_count={}
        n=len(s)
        for i in range(n):
            if t[i] not in t_count:
                t_count[t[i]]=1
            else:
                t_count[t[i]]+=1
        for i in range(n):
            if s[i] not in s_count:
                s_count[s[i]]=1
            else:
                s_count[s[i]]+=1

        if s_count==t_count:
            return True
        else:
            return False
        