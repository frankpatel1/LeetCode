class Fancy {

    private static final long MOD = 1_000_000_007L;

    private List<Long> nums;
    private long mul;
    private long add;

    public Fancy() {
        nums = new ArrayList<>();
        mul = 1;
        add = 0;
    }

    public void append(int val) {
        long inv = modPow(mul, MOD - 2);
        long stored = ((val - add) % MOD + MOD) % MOD;
        stored = (stored * inv) % MOD;
        nums.add(stored);
    }

    public void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    public void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    public int getIndex(int idx) {
        if (idx >= nums.size()) {
            return -1;
        }

        long value = (nums.get(idx) * mul + add) % MOD;
        return (int) value;
    }

    private long modPow(long base, long exp) {
        long res = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }

        return res;
    }
}