class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        fastest = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                fastest = max(fastest, nums[i] + i)
            
            l = r + 1
            r = fastest
            res += 1
        return res