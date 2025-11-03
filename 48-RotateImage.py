import numpy as np
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        #a = np.matrix
        # num_rows = np.shape(a)[0]
        
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1,  n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            #matrix[i].reverse()
            matrix[i] = matrix[i][::-1]

        
#time comnp:O(n^2)
#space comp: o(1)

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    print(matrix)
    print(obj.rotate(matrix))
    print(matrix)


if __name__ == "__main__":
    main()