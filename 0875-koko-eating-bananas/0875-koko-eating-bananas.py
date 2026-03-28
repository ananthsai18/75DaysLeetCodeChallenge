class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=-1
        while(left<=right):
            mid=(left+right)//2
            total=0
            for pile in piles:
                total+=ceil(pile/mid)
            if total<=h:
                res=mid
                right= mid-1
            else:
                left =mid+1
        return res
        