class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                tr_sum = nums[l] + nums[r] + a
                if tr_sum < 0:
                    l += 1
                elif tr_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
