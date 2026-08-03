class Solution {

    class DSU {
        int[] parent, size;
        int components;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            components = n;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        boolean union(int a, int b) {
            int pa = find(a);
            int pb = find(b);

            if (pa == pb) return false;

            if (size[pa] < size[pb]) {
                int temp = pa;
                pa = pb;
                pb = temp;
            }

            parent[pb] = pa;
            size[pa] += size[pb];
            components--;
            return true;
        }
    }

    public int maxStability(int n, int[][] edges, int k) {

        DSU dsu = new DSU(n);
        int minMust = Integer.MAX_VALUE;
        boolean hasMust = false;

        // Add mandatory edges
        for (int[] e : edges) {
            if (e[3] == 1) {
                hasMust = true;
                minMust = Math.min(minMust, e[2]);
                if (!dsu.union(e[0], e[1]))
                    return -1; // mandatory edges form cycle
            }
        }

        // Check graph connectivity
        for (int[] e : edges)
            dsu.union(e[0], e[1]);

        if (dsu.components != 1)
            return -1;

        int hi;
        if (hasMust) {
            hi = minMust;
        } else {
            hi = 0;
            for (int[] e : edges)
                hi = Math.max(hi, e[2] * 2);
        }

        int lo = 1;

        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (check(n, edges, k, mid))
                lo = mid;
            else
                hi = mid - 1;
        }

        return lo;
    }

    private boolean check(int n, int[][] edges, int k, int limit) {

        DSU dsu = new DSU(n);

        // Mandatory edges must satisfy limit
        for (int[] e : edges) {
            if (e[3] == 1) {
                if (e[2] < limit)
                    return false;
                dsu.union(e[0], e[1]);
            }
        }

        // Normal edges already satisfying limit
        for (int[] e : edges) {
            if (e[3] == 0 && e[2] >= limit)
                dsu.union(e[0], e[1]);
        }

        int upgrades = k;

        // Upgrade eligible edges if needed
        for (int[] e : edges) {
            if (upgrades == 0) break;

            if (e[3] == 0 && e[2] < limit && e[2] * 2 >= limit) {
                if (dsu.union(e[0], e[1]))
                    upgrades--;
            }
        }

        return dsu.components == 1;
    }
}