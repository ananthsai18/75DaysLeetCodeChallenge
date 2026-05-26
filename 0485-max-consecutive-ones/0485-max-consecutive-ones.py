class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1=0
        c=0
        for i in nums:
            if i==1:
                c+=1
            else:
                max_1=max(max_1,c)
                c=0
        max_1=max(max_1,c)
        return max_1

        