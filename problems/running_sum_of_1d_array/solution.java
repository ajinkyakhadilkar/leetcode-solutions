class Solution {
    public int[] runningSum(int[] nums) {
        int[] resultArray = new  int[nums.length];
        for(int i=0; i<nums.length; i++) {
            if(i==0) {
                resultArray[i] = nums[i];
            }
            else{
                resultArray[i] = resultArray[i-1] + nums[i];
            }
        }
        return resultArray;
    }
}