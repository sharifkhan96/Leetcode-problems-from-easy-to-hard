class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for curr_amount in range(1, amount+1):
            for coin in coins:
                if curr_amount - coin >= 0:
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])


        return dp[amount] if dp[amount] != float('inf') else -1

# time comp: O(amount*numb of coins)
# space comp: O(amount)


class main():
    coins = [1,2,5]
    amount = 11
    obj1 = Solution()
    print(obj1.coinChange(coins, amount))




if __name__ == "__main__":
    main()