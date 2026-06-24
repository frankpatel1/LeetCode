class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> isPrime(right + 1, true);
        isPrime[0] = isPrime[1] = false;

        for (long long i = 2; i * i <= right; i++) {
            if (isPrime[i]) {
                for (long long j = i * i; j <= right; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        vector<int> primes;
        for (int i = max(2, left); i <= right; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
            }
        }

        if (primes.size() < 2) {
            return {-1, -1};
        }

        vector<int> ans = {primes[0], primes[1]};
        int minGap = primes[1] - primes[0];

        for (int i = 2; i < primes.size(); i++) {
            int gap = primes[i] - primes[i - 1];

            if (gap < minGap) {
                minGap = gap;
                ans = {primes[i - 1], primes[i]};
            }

            // Twin primes: smallest possible gap
            if (minGap == 2) {
                break;
            }
        }

        return ans;
    }
};