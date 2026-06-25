class Solution {
    public String defangIPaddr(String address) {

        String mf="";
        for(int i=0;i<address.length();i++){
           char ch=address.charAt(i);

            if (ch=='.'){
                mf+="[.]";
            }else{
                mf+=ch;
            }
        }
        return mf;
    }
}