class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rowUp = 0 
        rowDown = len(matrix)-1
        rowFix = 0
        left = 0
        right = len(matrix[0])-1

        while rowUp <= rowDown :
            mid = (rowUp + rowDown) // 2

            if matrix[mid][left] <= target <= matrix[mid][right] :
                rowFix = mid 
                break

            elif matrix[mid][left] > target :
                rowDown = mid - 1
                
            elif matrix[mid][right] < target :
                rowUp = mid + 1

        while left <= right :

            mid = (left + right) // 2

            if matrix[rowFix][mid] == target :
                return True

            elif matrix[rowFix][mid] < target :
                left = mid + 1

            else :
                right = mid - 1

        return False 

            