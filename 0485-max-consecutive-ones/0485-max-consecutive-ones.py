class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        c=0
        for i in nums:
            if i==1:
                k+=1
            else:
                c=max(k,c)
                k=0
        c=max(k,c)
        return c
        