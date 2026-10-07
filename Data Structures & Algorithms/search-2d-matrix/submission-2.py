class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r and l>=0 and r <= n*m-1:
            mi = l + (r-l)//2
            n1 = mi // m
            n2 = mi - n1*m
            mid = matrix[n1][n2]

            if mid == target:
                return True
            elif mid < target:
                l = mi + 1
            elif mid > target:
                r = mi - 1
        
        return False

        