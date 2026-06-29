class Solution {
    public int numJewelsInStones(String jewels, String stones) {

        HashMap<Character,Integer> dici=new HashMap<Character,Integer>();

        for(int i=0;i<jewels.length();i++){
            char c=jewels.charAt(i);
            dici.put(c,0);
        }   

        for(int i=0;i<stones.length();i++){
            char ch=stones.charAt(i);
            if(dici.containsKey(ch)){
                int val=dici.get(ch);
                dici.put(ch,val+1);
            }
        }

        int k=0;
        for(Character i:dici.keySet()){
            k+=dici.getOrDefault(i,0);
        }
        return k;
    }
}