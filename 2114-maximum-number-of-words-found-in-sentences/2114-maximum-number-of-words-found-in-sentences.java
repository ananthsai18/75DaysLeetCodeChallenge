class Solution {
    public int mostWordsFound(String[] sentences) {

        int ans=0;

        for(int i=0;i<sentences.length;i++){
            String k=sentences[i];
            String arr[]=k.split("[\\s]+");
            ans=Math.max(ans,arr.length);
        }

        return ans;
        
    }
}