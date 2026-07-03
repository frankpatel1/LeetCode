from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Build the graph adjacency list
        # graph[u] = [(v, cost)]
        graph = [[] for _ in range(n)]
        unique_costs = set()
        
        for u, v, cost in edges:
            # We can skip the edge entirely if either the source or destination is offline
            if online[u] and online[v]:
                graph[u].append((v, cost))
                unique_costs.add(cost)
                
        # Sorted unique costs for our binary search space
        possible_scores = sorted(list(unique_costs))
        
        # In-degree computation for topological sort
        in_degree = [0] * n
        for u in range(n):
            for v, _ in graph[u]:
                in_degree[v] += 1
                
        # Find topological order of the DAG
        topo_order = []
        queue = [i for i in range(n) if in_degree[i] == 0]
        
        # Standard Kahn's algorithm for topological sorting
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            topo_order.append(u)
            for v, _ in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        def check(mid_score: int) -> bool:
            # dp[i] will store the minimum total cost to reach node i from node 0
            dp = [float('inf')] * n
            dp[0] = 0
            
            # Process nodes in topological order
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                for v, cost in graph[u]:
                    # Only consider edges with cost >= mid_score
                    if cost >= mid_score:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Binary search over the indices of possible scores
        low, high = 0, len(possible_scores) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(possible_scores[mid]):
                ans = possible_scores[mid]  # Found a valid score, try to look for a higher one
                low = mid + 1
            else:
                high = mid - 1
                
        return ans