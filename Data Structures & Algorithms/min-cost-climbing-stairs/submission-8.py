class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 3:
            return min(cost)
        
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[-1]