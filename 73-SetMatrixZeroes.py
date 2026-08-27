class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # space efficient sol:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

# O(M+N) & O(1) for tiime & space complexiities    
# -----------------------------

        # R = len(matrix)
        # C = len(matrix[0])

        # rows_set, cols_set = set(), set()

        # # finding origianl zeros
        # for r in range(R):
        #     for c in range(C):
        #         if matrix[r][c] == 0:
        #             rows_set.add(r)
        #             cols_set.add(c)

        # # set corresponding rows/cols to zero
        # for r in range(R):
        #     for c in range(C):
        #         if r in rows_set or c in cols_set:
        #             matrix[r][c] = 0 


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