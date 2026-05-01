class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        s=set()
        j=0
        while j<n:
            if nums[j] not in s:
                nums[i]=nums[j]
                s.add(nums[j])
                i+=1
            j+=1
        return i

        