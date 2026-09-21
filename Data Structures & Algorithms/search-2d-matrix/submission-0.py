class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        row = -1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            if target > matrix[mid][0]:
                l = mid + 1
            else:
                h = mid - 1
        if row == -1:
            return False
        return self.bsearch(matrix[mid], target)

    def bsearch(self, arr, target):
        l, h = 0, len(arr) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == target:
                return True
            if target > arr[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return False
