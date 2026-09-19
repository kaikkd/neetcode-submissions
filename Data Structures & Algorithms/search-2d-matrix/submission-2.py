class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for m in range(len(matrix)):
            if matrix[m][-1] < target:
                continue
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[m][mid] < target:
                    l += 1
                elif matrix[m][mid] > target:
                    r -= 1
                else:
                    return True
        
        return False