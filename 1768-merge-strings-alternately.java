class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ans = new String();
        int len = Math.min(word1.length(), word2.length());
        for (int i = 0; i < len; i++) {
            ans += word1.charAt(i);
            ans += word2.charAt(i);
        }
        ans += (word1.substring(len));
        ans += (word2.substring(len));
        return ans;
    }
}
