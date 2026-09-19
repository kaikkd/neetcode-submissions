class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, ROW * COL - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // COL, mid % COL
            if matrix[row][col] < target:
                l += 1
            elif matrix[row][col] > target:
                r -= 1
            else:
                return True

        return False