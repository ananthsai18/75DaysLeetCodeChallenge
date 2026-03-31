class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        n=len(nums2)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums2[j]>nums2[i]:
                    dic[nums2[i]]=nums2[j]
                    break
                
        result=[]
        for i in nums1:
            if i in dic:
                result.append(dic[i])
            else:
                result.append(-1)
        return result

        