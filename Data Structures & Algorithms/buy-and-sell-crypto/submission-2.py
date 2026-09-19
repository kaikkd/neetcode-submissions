class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_p = 0

        l, r = 0, 1
        while r <= len(prices) - 1:
            if prices[l] < prices[r]:
                cur_p = prices[r] - prices[l]
                max_p = max(max_p, cur_p)
                r += 1
            else:
                l = r
                r += 1
        
        return max_p