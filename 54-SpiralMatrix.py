class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        rows, columns = len(matrix), len(matrix[0])
        top = left = 0
        right = columns - 1
        down = rows - 1

        # left, right = 0, len(matrix[0])
        # top, bottom = 0, len(matrix)
        result = []

        #while left < right and top < bottom:
        while len(result) < rows * columns:
            # traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # traverse downwards
            for row in range(top, down + 1):
                result.append(matrix[row][right])
            right -= 1

            # make sure we are now on a diff row
            if top <= down:
                # traver from right to left
                for col in range(right, left - 1, -1):
                    result.append(matrix[down][col])
                down -= 1
            
            # make sure we are now on a diff column
            if left <= right:
                # traverse upwards
                for row in range(down, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result

# O(M*N) & O(1) time & space comps

def print_matrix(matrix):
    for row in matrix:
        print(row)


class main():
    obj = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(matrix)
    print("----------")
    print("Resulted spiral matrix: ", obj.spiralOrder(matrix))
    print("----------")
    print_matrix(matrix)


if __name__ == "__main__":
    main()