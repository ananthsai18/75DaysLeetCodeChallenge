class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
      
        for i in dic:
            if dic[i]>2:
                return False
        return True

        