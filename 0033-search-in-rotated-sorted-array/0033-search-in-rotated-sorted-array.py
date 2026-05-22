class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        h=n-1


        while (l<=h):
            m=(l+h)//2

            if nums[m]==target:
                return m
            
            elif nums[m]<=nums[n-1]:
                if target < nums[m]:
                    h=m-1
                else:
                    if target <= nums[n-1]:
                        l=m+1
                    else:
                        h=m-1
            
            else:
                if target > nums[m]:
                    l=m+1
                else:
                    if target < nums[0]:
                        l=m+1
                    else:
                        h=m-1
               
        return -1


        