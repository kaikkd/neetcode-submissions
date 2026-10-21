class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        fatest = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                fatest = max(fatest, i + nums[i])
            l = r + 1
            r = fatest
            res += 1
        
        return res