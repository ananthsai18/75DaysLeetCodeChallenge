class Solution {
    public int[] replaceElements(int[] arr) {
        int i=0;
        int n=arr.length;
        int j=n-2;
        int max=arr[n-1];
        while(j>=0){
            int temp=arr[j];
            arr[j]=max;
            max=Math.max(temp,arr[j]);
            j-=1;
        }
        arr[n-1]=-1;
        return arr;
    }
}