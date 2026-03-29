class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=-1
        while(l<=r):
            m=(l+r)//2
            total=0
            days_taken=1
            for i in weights:
                if (total+i)<=m:
                    total+=i
                else:
                    days_taken+=1
                    total=i
            if days_taken <= days:
                res=m
                r=m-1
            else:
                l=m+1
        return res
        