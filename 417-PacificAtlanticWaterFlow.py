from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        # Add left and right border cells
        for row in range(rows):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols - 1))

        # Add top and bottom border cells
        for col in range(cols):
            pacific_queue.append((0, col))
            atlantic_queue.append((rows - 1, col))

        def bfs(queue):
            reachable = set()

            while queue:
                row, col = queue.popleft()

                if (row, col) in reachable:
                    continue

                reachable.add((row, col))

                directions = [
                    (1, 0),    # down
                    (-1, 0),   # up
                    (0, 1),    # right
                    (0, -1)    # left
                ]

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    # Check boundaries
                    if (
                        new_row < 0
                        or new_row >= rows
                        or new_col < 0
                        or new_col >= cols
                    ):
                        continue

                    # Check whether already visited
                    if (new_row, new_col) in reachable:
                        continue

                    # Reverse BFS: move to equal or higher cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue

                    queue.append((new_row, new_col))

            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        common_cells = pacific_reachable.intersection(atlantic_reachable)

        return [list(cell) for cell in common_cells]


# Time complexity: O(rows * cols)
# Space complexity: O(rows * cols)


def main():
    matrix = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    obj1 = Solution()
    result = obj1.pacificAtlantic(matrix)

    print(result)


if __name__ == "__main__":
    main()