class Solution {
    public long countGood(int[] nums, int k) {
        int left = 0, right = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        int sum = 0;
        long count = 0;

        if (k == 0) {
            return nums.length * nums.length / 2;
        }

        outer:
        while(right < nums.length) {

            do {
                if(right >= nums.length) {
                    break outer;
                }
                hm.put(nums[right], hm.getOrDefault(nums[right], 0) + 1);
                sum += hm.get(nums[right]) - 1;
                right++;
            } while(sum < k);

            while(sum >= k) {
                int sub = hm.get(nums[left]) - 1;
                if (sum - sub >= k) {
                    sum -= sub;
                    hm.put(nums[left], hm.get(nums[left]) - 1);
                    left++;
                }
                else {
                    break;
                }
            }
            if (sum >= k) {
                count += left + 1;
            }
        }
        return count;
    }
}
