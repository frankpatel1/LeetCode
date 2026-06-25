class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int n = words.size();
        int i = 0;

        while (i < n) {
            int j = i;
            int lineLen = 0;

            while (j < n &&
                   lineLen + words[j].size() + (j - i) <= maxWidth) {
                lineLen += words[j].size();
                j++;
            }

            int gaps = j - i - 1;
            string line;

            // Last line or single word
            if (j == n || gaps == 0) {
                line = words[i];

                for (int k = i + 1; k < j; k++) {
                    line += " " + words[k];
                }

                line += string(maxWidth - line.size(), ' ');
            }
            else {
                int totalSpaces = maxWidth - lineLen;
                int evenSpaces = totalSpaces / gaps;
                int extraSpaces = totalSpaces % gaps;

                for (int k = i; k < j - 1; k++) {
                    line += words[k];
                    line += string(
                        evenSpaces + (extraSpaces > 0 ? 1 : 0),
                        ' '
                    );

                    if (extraSpaces > 0)
                        extraSpaces--;
                }

                line += words[j - 1];
            }

            result.push_back(line);
            i = j;
        }

        return result;
    }
};