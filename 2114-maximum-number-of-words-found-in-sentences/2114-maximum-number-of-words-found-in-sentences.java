class Solution {
    public int mostWordsFound(String[] sentences) {

        int ans=0;

        for(int i=0;i<sentences.length;i++){
            String k=sentences[i];
            int temp=0;
            String arr[]=k.split("[\\s]+");
            // for(int p=0;p<arr.length;p++){
            //     System.out.println(arr[p]);
            // }

            for(int j=0;j<arr.length;j++){
                temp+=1;
            }
            ans=Math.max(ans,temp);
        }

        return ans;
        
    }
}