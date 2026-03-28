class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n<m*k:
            return -1

        left=min(bloomDay)
        right=max(bloomDay)
        result=-1
        while(left<=right):
            mid=(left+right)//2
            flowers=0
            bouquets=0
            for i in bloomDay:
                if i<=mid:
                    flowers+=1

                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
            if bouquets>=m:
                result=mid
                right=mid-1
            else:
                left=mid+1
        if result == -1:
            return -1
        else:
            return result