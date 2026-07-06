class Solution {
public:
    unordered_set<string> dict;
    unordered_map<int, vector<string>> memo;

    vector<string> dfs(string &s, int start) {

        if (memo.count(start))
            return memo[start];

        if (start == s.size())
            return {""};

        vector<string> res;

        string word;

        for (int end = start; end < s.size(); end++) {

            word.push_back(s[end]);

            if (!dict.count(word))
                continue;

            vector<string> suffix = dfs(s, end + 1);

            for (string &str : suffix) {

                if (str.empty())
                    res.push_back(word);
                else
                    res.push_back(word + " " + str);
            }
        }

        return memo[start] = res;
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {

        dict = unordered_set<string>(wordDict.begin(), wordDict.end());

        return dfs(s, 0);
    }
};