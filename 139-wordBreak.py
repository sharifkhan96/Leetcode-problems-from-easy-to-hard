class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # classic forward dp
        # word_set = set(wordDict)  # O(1) lookups
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True  # base case: empty string

        # for i in range(1, n + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break  # no need to check further splits

        # return dp[n]

        # classic backward dp
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

# time complexity: O(n * m * k): n for outer loop, m for inner loop, k for slicing/comparison
# space complexity: O(n) for dp list

# Main function
def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    print("Can the string be segmented?", solution.wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
