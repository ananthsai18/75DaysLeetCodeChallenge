class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m*k)>len(bloomDay):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        while(left<right):
            bouqets=0
            flowers=0
            mid=(left+right)//2
            for d in bloomDay:
                if d<=mid:
                    flowers+=1
                    if flowers==k:
                        bouqets+=1
                        flowers=0
                else:
                    flowers=0
            if bouqets>=m:
                right=mid
            else:
                left=mid+1
        return left

        