class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0

        l, r = 0, len(heights) - 1
        while l < r:
            cur_w = (r - l) * min(heights[l], heights[r])
            max_w = max(cur_w, max_w)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_w