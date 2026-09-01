from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            # we matched every character
            if i == len(word):
                return True

            # ut of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # current cell doesn't match
            if board[r][c] != word[i]:
                return False

            # mmark this cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # backtrack
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# Time: O(m × n × 4^L) approximately
# Space: O(L) for the recursion stack


# Main function
def main():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    solution = Solution()

    for word in ["ABCCED", "SEE", "ABCB"]:
        print(f"Does '{word}' exist?", solution.exist(board, word))


if __name__ == "__main__":
    main()