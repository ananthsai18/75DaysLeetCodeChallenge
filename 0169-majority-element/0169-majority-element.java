class Solution {
    public int majorityElement(int[] nums) {
        int n= nums.length;
        HashMap<Integer,Integer> dici=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            int val=nums[i];
            if(dici.containsKey(val))
            {
                int crnt_val=dici.get(val);
                dici.put(val,crnt_val+1);
            }else
            {
                dici.put(val,1);
            }
        }

        int max=0;
        for(int val:dici.keySet()){
            if(dici.get(val)> n/2){
                max=val;
            }
        }

        return max;
    }
}