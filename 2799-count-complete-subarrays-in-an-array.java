class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int count = 0;
        HashSet set = new HashSet<Integer>();
        for(int i : nums) {
            set.add(i);
        }
        int size = set.size();
        for(int i = 0; i < nums.length; i++) {
            HashSet subset = new HashSet<Integer>();
            for(int j = i; j < nums.length; j++) {
                subset.add(nums[j]);
                if(subset.size() == size){
                    count++;
                }
            }
        }
        return count;
    }
}
