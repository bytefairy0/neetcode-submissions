class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        si, sj = 0, 0
        ei, ej = m-1, n-1

        targetRow = 0

        # find Target row
        while si<=ei:
            mid_i = si + (ei-si)//2
            if target > matrix[mid_i][n-1]:
                si = mid_i+1
            elif target < matrix[mid_i][0]:
                ei = mid_i-1
            else:
                targetRow = mid_i
                break
        
        # find widin targeted row
        while sj<=ej:
            mid_j = sj + (ej-sj)//2
            if target == matrix[targetRow][mid_j]:
                return True
            elif target < matrix[targetRow][mid_j]:
                ej = mid_j-1
            else:
                sj = mid_j+1
        return False