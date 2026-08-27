class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])

        rows_set, cols_set = set(), set()

        # finding origianl zeros
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rows_set.add(r)
                    cols_set.add(c)

        # set corresponding rows/cols to zero
        for r in range(R):
            for c in range(C):
                if r in rows_set or c in cols_set:
                    matrix[r][c] = 0 


# O(M+N) & O(M+N) for tiime & space complexiities

def print_matrix(matrix):
    for row in matrix:
        print(row)


class main():
    obj = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print_matrix(matrix)
    print("----------")
    obj.setZeroes(matrix)
    print_matrix(matrix)


if __name__ == "__main__":
    main()