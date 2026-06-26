class Solution {
    public int maxDistance(int[] colors) {
        int n=colors.length;
        int ans=-1;
        int prev=-1000;
        for(int i=0;i<n;i++){
            if(colors[i]!=prev){

                for(int j=i+1;j<n;j++){
                if (colors[i]!=colors[j]){
                    ans=Math.max(ans,Math.abs(j-i));
                }
            }

            }
           
            prev=colors[i];
        }
        return ans;
    }
}