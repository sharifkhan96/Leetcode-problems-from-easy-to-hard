class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        
        for account in accounts:
            current_wealth = sum(account)

            max_wealth = max(max_wealth, current_wealth)

        return max_wealth



def main():
    accounts = [[1, 2, 3], [3, 7, 1], [3, 4, 5, 6, 2]]
    obj1 = Solution()

    result = obj1.maximumWealth(accounts)
    print(f"Maximum of the {accounts} sums up to: {result}")


if __name__ == "__main__":
    main()
        