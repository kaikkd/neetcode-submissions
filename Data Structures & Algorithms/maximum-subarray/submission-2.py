class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cnt = nums[0], 0

        for n in nums:
            if cnt <= 0:
                cnt = 0
            cnt += n
            res = max(cnt, res)
        
        return res