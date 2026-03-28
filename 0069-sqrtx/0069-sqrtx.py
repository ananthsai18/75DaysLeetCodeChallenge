class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        res=-1
        while(l<=r):
            m=(l+r)//2
            sq=m*m
            if sq<=x:
                res=m
                l=m+1
            else:
                r=m-1
        return res
        