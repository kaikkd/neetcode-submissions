class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums = set(nums)

        for n in nums:
            if n - 1 in nums:
                continue
            
            cur_num = n
            cur_length = 1
            while cur_num + 1 in nums:
                cur_num += 1
                cur_length += 1
            
            max_length = max(max_length, cur_length)
        
        return max_length