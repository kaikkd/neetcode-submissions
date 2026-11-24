class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        if n <= 3:
            return min(cost)
        
        dp = [0] * n

        dp[2] = min(cost[0], cost[1])
        for i in range(3, n):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[-1]