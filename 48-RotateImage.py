import numpy as np
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        left, right = 0, len(matrix) -1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the topleft somewhere
                topLeft = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1

# time & space complexities: O(M) & O(1)
# --------------------------------------------------------------

        # #a = np.matrix
        # # num_rows = np.shape(a)[0]
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i + 1,  n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # for i in range(n):
        #     #matrix[i].reverse()
        #     matrix[i] = matrix[i][::-1]       
#time comnp:O(n^2)
#space comp: o(1)

#------------------------------------------------------------

    # transpose & reverse for the matrix rotation
    #     self.transpose(matrix)
    #     self.reflect(matrix)

    # def transpose(self, matrix):
    #     n = len(matrix)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # def reflect(self, matrix):
    #     n = len(matrix)
    #     for i in range(n):
    #         for j in range(n // 2):
    #             matrix[i][j], matrix[i][-j - 1] = (
    #                 matrix[i][-j - 1],
    #                 matrix[i][j],
    #             )
    # time & space complexities: O(M) & O(1)         




def printMatrix(matrix):
    for row in matrix:
        print(row)



def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    printMatrix(matrix)
    print("----------")
    obj.rotate(matrix)
    printMatrix(matrix)


if __name__ == "__main__":
    main()