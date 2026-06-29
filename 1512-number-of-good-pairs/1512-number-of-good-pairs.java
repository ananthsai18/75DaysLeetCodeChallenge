class Solution {
    public int numIdenticalPairs(int[] nums) {

        HashMap<Integer,Integer> dic=new HashMap<Integer,Integer>();

        for(int i=0;i<nums.length;i++){
            dic.put(nums[i],dic.getOrDefault(nums[i],0)+1);
        }
        
        int pairs=0;
        for(int k:dic.keySet()){
            int p=dic.get(k);
            int c=p*(p-1)/2;
            pairs+=c;
        }

        return pairs;
    }
}