class Solution:
    def numDecodings(self, s: str) -> int:
        # memoized solution: time and space: O(N) & O(N)
        # memo = {}
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     ans = dfs(i + 1)

        #     if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         ans += dfs(i + 2)

        #     memo[i] = ans
        #     return ans

        # return dfs(0)
    
        # space optimized solution: time & space: O(N) and O(1)
        # n = len(s)
        # first, second = 1, 0

        # for i in range(n-1, -1, -1):
        #     if s[i] == '0':
        #         return 0
        #         #curr = 0
        #     else:
        #         curr = first
        #         if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
        #             curr += second if i + 2 <= n else 0

        #     first, second = curr, first

        # return first
            

        # bottom up dp solution: time and space: O(N) & O(N)
        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                #dp[i] = 0
                return 0  
            else:
                dp[i] = dp[i + 1]

                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
        return dp[0]




def main():
    obj = Solution()
    s = "226"
    print(f'There are {obj.numDecodings(s)} ways to decode {s}')


if __name__ == "__main__":
    main()