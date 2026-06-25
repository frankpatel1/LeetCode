class Solution {
public:
    unordered_map<string, bool> memo;

    bool solve(string s1, string s2) {
        if (s1 == s2)
            return true;

        string key = s1 + "#" + s2;

        if (memo.count(key))
            return memo[key];

        vector<int> freq(26, 0);

        for (char c : s1) freq[c - 'a']++;
        for (char c : s2) freq[c - 'a']--;

        for (int x : freq) {
            if (x != 0)
                return memo[key] = false;
        }

        int n = s1.size();

        for (int k = 1; k < n; k++) {

            // No swap
            if (solve(s1.substr(0, k), s2.substr(0, k)) &&
                solve(s1.substr(k), s2.substr(k)))
                return memo[key] = true;

            // Swap
            if (solve(s1.substr(0, k), s2.substr(n - k)) &&
                solve(s1.substr(k), s2.substr(0, n - k)))
                return memo[key] = true;
        }

        return memo[key] = false;
    }

    bool isScramble(string s1, string s2) {
        return solve(s1, s2);
    }
};