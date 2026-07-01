class Solution {
    public int[] findErrorNums(int[] nums) {

        HashSet<Integer> m=new HashSet<>();
        int duplicate=-1 ;
        for(int i=0;i<nums.length;i++){
            if ( ! m.contains(nums[i])){
                m.add(nums[i]);
                
            }else{
                duplicate=nums[i];
               
            }
        }

        int missing =-1;
        for(int i=1;i<=nums.length;i++){
            if(!m.contains(i)){
                missing=i;
                break;
            }
        }
        
        return new int[]{duplicate,missing};
        
    }
}