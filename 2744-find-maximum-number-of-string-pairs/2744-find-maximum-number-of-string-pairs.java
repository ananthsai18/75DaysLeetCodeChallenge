class Solution {

    public static String rev(String s){
        String k="";

        for(int p= s.length()-1 ;p>=0;p--){
            k+= s.charAt(p);
        }
        return k;
    }


    public int maximumNumberOfStringPairs(String[] words) {

     int ans=0;

     for(int i=0;i<words.length;i++){
        String k=rev(words[i]);
        for(int j=i+1;j<words.length;j++){
            if(words[j].equals(k)){
                ans+=1;
            }
        }
     }  
     return ans; 
        
    }
}