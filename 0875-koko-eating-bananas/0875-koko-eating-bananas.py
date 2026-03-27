import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        n=len(piles)
        ans=right
        while(left<=right):
            total=0
            mid=(left+right)//2
            for pile in piles:
                total+=math.ceil(pile/mid)
            # print(total,mid)
            if total<=h:
                ans= mid
                right=mid-1
            else:
                left=mid+1
        return ans
        