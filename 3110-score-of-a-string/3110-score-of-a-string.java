class Solution {
    public int scoreOfString(String s) {

        int n=s.length();

        char a=s.charAt(0);
        int sum=0;
        for(int i=1;i<n;i++){
            char b=s.charAt(i);
            sum+=Math.abs(a-b);
            a=b;
        }
        return sum;
        
    }
}