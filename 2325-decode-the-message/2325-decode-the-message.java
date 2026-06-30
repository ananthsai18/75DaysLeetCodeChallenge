class Solution {
    public String decodeMessage(String key, String message) {
        HashMap<Character,Character> dc=new HashMap<Character,Character>();
        int a=97;
        for(int i=0;i<key.length();i++){
            if(key.charAt(i)!= ' ' && !dc.containsKey(key.charAt(i))){
                dc.put(key.charAt(i), (char) a);
                a+=1;
            }
        }

        // System.out.println(dc);


        String ans = "";
        for(int i=0;i<message.length();i++){
            if (message.charAt(i)==' '){
                ans+=' ';
            }else{
                ans+=dc.get(message.charAt(i));
            }
        }
        return ans;
    }
}