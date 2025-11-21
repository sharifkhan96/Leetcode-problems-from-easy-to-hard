class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create DP table with all 1s in first row and first column
        dp = [[1] * n for _ in range(m)]
        
        # flling the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# time comp: O(m*n)
# space comp: //

class main():
    m = 3,
    n = 7    
    obj1 = Solution()
    print(obj1.uniquePaths(m, n))



if __name__ == "__main__":
    main()