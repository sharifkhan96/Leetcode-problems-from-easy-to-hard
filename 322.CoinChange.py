from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Initialize dp array with "infinity"
        dp = [float('inf')] * (amount + 1)
        
        # Base case
        dp[0] = 0
        
        # Build dp table
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        
        
        # If amount not reachable
        return dp[amount] if dp[amount] != float('inf') else -1

# tiem and space complexities: O(m * n) and O(n) respectively

def main():
    coins = [1, 2, 5]
    amount = 11
    
    obj = Solution()
    result = obj.coinChange(coins, amount)
        
    print("Coins:", coins)
    print("Amount:", amount)
    print("Minimum coins needed:", result)


if __name__ == "__main__":
    main()