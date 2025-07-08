class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        #print(coordinates)
        column = coordinates[0]
        row = coordinates[1]

        chessboard_column_index = ord(column) - ord('a') + 1
        chessboard_row_index = int(row)

        if (chessboard_column_index + chessboard_row_index) % 2 == 0:
            return False
        else:
            return True

# time: O(1)
# space: O(1)


def main():

    #coordinates = [[1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8]]
    chessboard_coordinates = input("provide the string of a chessboard: ")
    obj = Solution()
    result = obj.squareIsWhite(chessboard_coordinates)
    print(result)


if __name__ == "__main__":
    main()