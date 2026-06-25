class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int jwls=0;

        for(int i=0;i<jewels.length();i++){
            char a=jewels.charAt(i);
            for(int j=0;j<stones.length();j++){
                char b=stones.charAt(j);

                if (a==b){
                    jwls+=1;
                }
            }
        } 
        return jwls  ;   
    }
}