class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        l=1
        r=max(candies)
        res=-1
        while(l<=r):
            m=(l+r)//2
            if m==0:
                break
            students=0
            for c in candies:
                students+=(c//m)
        
            if students>=k:
                res=m
                l=m+1
            else:
                r=m-1

        return res
        