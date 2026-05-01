class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1          # ① -1 (last index, not length)

        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // cols                   # ② cols not matrix[0]
            c = mid % cols
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False