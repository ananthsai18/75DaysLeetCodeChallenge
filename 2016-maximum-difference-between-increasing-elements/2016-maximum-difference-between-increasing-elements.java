class Solution {
    public int maximumDifference(int[] nums) {
        int n=nums.length;
        int ans=-1;
        int min=nums[0];
        for(int j=1;j<n;j++){
            if (nums[j] > min){
                ans=Math.max(ans,nums[j]-min);
            }else{
                min=nums[j];
            }
        }
        return ans;
    }
}