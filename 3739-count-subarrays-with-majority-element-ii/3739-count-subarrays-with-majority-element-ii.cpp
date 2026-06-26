class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;

        BIT(int sz) : n(sz), bit(sz + 1, 0) {}

        void add(int idx, int val) {
            while (idx <= n) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        }

        int sum(int idx) {
            int res = 0;
            while (idx > 0) {
                res += bit[idx];
                idx -= idx & -idx;
            }
            return res;
        }
    };

    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();

        int offset = n + 2;
        BIT bit(2 * n + 5);

        long long ans = 0;
        int pref = 0;

        bit.add(offset, 1);   // prefix sum = 0

        for (int x : nums) {
            pref += (x == target ? 1 : -1);

            int idx = pref + offset;

            ans += bit.sum(idx - 1);

            bit.add(idx, 1);
        }

        return ans;
    }
};