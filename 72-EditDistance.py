class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # here we create aDP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # our base cases
        for i in range(m + 1):
            dp[i][0] = i   # deletnggg i characters
        
        for j in range(n + 1):
            dp[0][j] = j   # insertingggggg j characters


        # filling the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # in here ,no edit needed

                else:
                    insert  = dp[i][j - 1] + 1
                    delete  = dp[i - 1][j] + 1
                    replace = dp[i - 1][j - 1] + 1

                    dp[i][j] = min(insert, delete, replace)

        return dp[m][n]


def main():
    obj = Solution()
    print(obj.minDistance("horse", "ros")) 

if __name__ == "__main__":
    main()
