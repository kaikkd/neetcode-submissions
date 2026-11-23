class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}

        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        
        count_num = []
        for num, count in num_dict.items():
            count_num.append([count, num])
        
        count_num.sort()

        res = []
        while k > 0:
            k -= 1
            res.append(count_num.pop()[1])
        
        return res