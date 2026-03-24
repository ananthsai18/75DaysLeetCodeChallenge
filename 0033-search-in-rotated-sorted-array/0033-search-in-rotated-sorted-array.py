class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            guess=(low+high)//2
            if nums[guess]==target:
                return guess

            elif nums[guess]<nums[n-1]:
                if target<nums[guess]:
                    high=guess-1
                else:
                    if target <=nums[n-1]:
                        low=guess+1
                    else:
                        high=guess-1
            else:
                if target>nums[guess]:
                    low=guess+1
                else:
                    if target<nums[0]:
                        low=guess+1
                    else:
                        high=guess-1
        return -1