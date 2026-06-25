class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int ans = 0;
        int n = heights.size();

        for (int i = 0; i <= n; i++) {
            int curr = (i == n ? 0 : heights[i]);

            while (!st.empty() && heights[st.top()] > curr) {
                int h = heights[st.top()];
                st.pop();

                int left = st.empty() ? -1 : st.top();
                int width = i - left - 1;

                ans = max(ans, h * width);
            }

            st.push(i);
        }

        return ans;
    }

    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;

        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<int> heights(cols, 0);
        int ans = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == '1')
                    heights[c]++;
                else
                    heights[c] = 0;
            }

            ans = max(ans, largestRectangleArea(heights));
        }

        return ans;
    }
};