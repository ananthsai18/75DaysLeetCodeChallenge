class Solution {
    public boolean isIsomorphic(String s, String t) {

        HashMap<Character,Character> dic=new HashMap<Character,Character>();
        HashMap<Character,Character> r_dic=new HashMap<Character,Character>();
        
        int n=s.length();
        if(n!=t.length()){
            return false;
        }

        for(int i=0;i<n;i++){
           char s1=s.charAt(i);
            char t1=t.charAt(i);

            if(!dic.containsKey(s1) && !r_dic.containsKey(t1)){
                dic.put(s1,t1);
                r_dic.put(t1,s1);

            }else if(dic.containsKey(s1)){
                if(dic.get(s1)!=t1){
                    return false;
                }
            }else if(r_dic.containsKey(t1)){
                if(r_dic.get(t1)!=s1){
                    return false;
                }
            }else{
                return false;
            } 
        }
        return true;
    }
}