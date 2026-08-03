class Solution {

    private int count = 0;
    private String ans = "";

    public String getHappyString(int n, int k) {
        StringBuilder sb = new StringBuilder();
        dfs(n, k, sb);
        return ans;
    }

    private void dfs(int n, int k, StringBuilder sb) {
        if (!ans.isEmpty()) return;

        if (sb.length() == n) {
            count++;
            if (count == k) {
                ans = sb.toString();
            }
            return;
        }

        for (char ch = 'a'; ch <= 'c'; ch++) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ch) {
                continue;
            }

            sb.append(ch);
            dfs(n, k, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}