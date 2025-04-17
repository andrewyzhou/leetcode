class Solution {
    public int countPairs(int[] nums, int k) {
        int count = 0;
        HashMap<Integer,ArrayList<Integer>> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            ArrayList<Integer> indices = hm.getOrDefault(nums[i], new ArrayList<Integer>());
            indices.add(i);
            hm.put(nums[i], indices);
        }
        for(ArrayList<Integer> value : hm.values()) {
            for(int i = 0; i < value.size(); i++) {
                for(int j = i + 1; j < value.size(); j++){
                    if (value.get(i) * value.get(j) % k == 0) {
                        count ++;
                    }
                }
            }
        }
        return count;
    }
}
