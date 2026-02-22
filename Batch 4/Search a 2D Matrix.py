from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        LeetCode #74 - Search a 2D Matrix (Medium)

        Approach:
            The matrix rows are sorted and the first element of each row is
            greater than the last element of the previous row, so the matrix
            is equivalent to a single sorted array of m*n elements. Treat it
            as such: map a virtual flat index `mid` to (mid // cols, mid % cols)
            to access the matrix in O(1). One binary search over [0, m*n - 1]
            locates the target.

        Time Complexity:  O(log(m * n)) — binary search over the flattened array.
        Space Complexity: O(1) — only scalar variables.
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]

    # Test 1: Target present in the middle
    assert sol.searchMatrix(matrix1, 3) is True

    # Test 2: Target absent
    assert sol.searchMatrix(matrix1, 13) is False

    # Test 3: Target is the first element
    assert sol.searchMatrix(matrix1, 1) is True

    # Test 4: Target is the last element
    assert sol.searchMatrix(matrix1, 60) is True

    # Test 5: Single-cell matrix, found
    assert sol.searchMatrix([[5]], 5) is True

    # Test 6: Single-cell matrix, not found
    assert sol.searchMatrix([[5]], 1) is False

    print("All test cases passed.")
