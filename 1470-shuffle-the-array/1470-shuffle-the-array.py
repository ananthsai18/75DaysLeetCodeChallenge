class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr=[0]*(n*2)
        print(arr)
        p=0
        for i in range(0,n):
            arr[p]=nums[i]
            arr[p+1]=nums[n+i]
            p+=2
        return arr