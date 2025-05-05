class Solution:
    def convert(self, s: str, numRows: int) -> str:
    
        if numRows == 1:
            return s
        
        rows = ["" for _ in range(numRows)]
        current_row = 0
        going_down = False   # it should not be going_down but rather tracker since it only tracks where are we..
        for i in range(len(s)):
            rows[current_row] += s[i]
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return rows, ''.join(rows)


def main():
    string1 = "PAYPALISHIRING"
    numRows = int(input("enter the number of row: "))
    obj1 = Solution()
    result = obj1.convert(string1, numRows)
    print(result)

if __name__ == "__main__":
    main()