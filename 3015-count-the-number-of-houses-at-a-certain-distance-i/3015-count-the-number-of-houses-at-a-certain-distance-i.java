class Solution {
    public int[] countOfPairs(int n, int x, int y) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Build the line graph
        for (int i = 1; i < n; i++) {
            graph[i].add(i + 1);
            graph[i + 1].add(i);
        }

        // Extra edge
        if (x != y) {
            graph[x].add(y);
            graph[y].add(x);
        }

        int[] ans = new int[n];

        for (int start = 1; start <= n; start++) {
            int[] dist = new int[n + 1];
            Arrays.fill(dist, -1);

            Queue<Integer> q = new LinkedList<>();
            q.offer(start);
            dist[start] = 0;

            while (!q.isEmpty()) {
                int u = q.poll();

                for (int v : graph[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.offer(v);
                    }
                }
            }

            for (int end = 1; end <= n; end++) {
                if (start != end) {
                    ans[dist[end] - 1]++;
                }
            }
        }

        return ans;
    }
}