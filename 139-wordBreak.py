class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)  # O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check further splits

        return dp[n]


# Main function
def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    print("Can the string be segmented?", solution.wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
