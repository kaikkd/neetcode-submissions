class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            cur = nums[i]
            if cur > 0:
                break
            if i > 0 and cur == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = cur + nums[l] + nums[r]
                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    res.append([cur, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res