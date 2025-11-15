class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            # we stp here if out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return

            # markingggggggg current land as visited (so sink it)
            grid[r][c] = "0"

            # here, weeee explore the  neighbors
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # scan the whole grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # found new island
                    count += 1
                    dfs(r, c)         # sink all land of this island

        return count



class main():
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    
    obj1 = Solution()
    print(obj1.numIslands(grid))




if __name__ == "__main__":
    main()