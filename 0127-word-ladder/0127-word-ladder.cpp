class Solution {
public:
    int ladderLength(string beginWord, string endWord,
                     vector<string>& wordList) {

        unordered_set<string> dict(wordList.begin(), wordList.end());

        if (!dict.count(endWord))
            return 0;

        queue<pair<string, int>> q;
        q.push({beginWord, 1});

        dict.erase(beginWord);

        while (!q.empty()) {

            auto [word, steps] = q.front();
            q.pop();

            if (word == endWord)
                return steps;

            string temp = word;

            for (int i = 0; i < temp.size(); i++) {

                char old = temp[i];

                for (char c = 'a'; c <= 'z'; c++) {

                    temp[i] = c;

                    if (dict.count(temp)) {

                        q.push({temp, steps + 1});

                        dict.erase(temp);
                    }
                }

                temp[i] = old;
            }
        }

        return 0;
    }
};