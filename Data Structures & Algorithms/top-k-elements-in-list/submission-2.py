class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1
        
        nums_count = [[count, num] for num, count in nums_dict.items()]
        nums_count.sort(key = lambda x : x[0])

        res = []
        while k > 0:
            res.append(nums_count.pop()[1])
            k -= 1
        
        return res