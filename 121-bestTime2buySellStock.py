class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # 1st approach, two pointer solution
        l, r = 0, 1 # l = buying, r = selling

        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r

            r += 1
        return max_profit

        
        # 2nd approach
        # min_price = float('inf')  # very large number
        # max_profit = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price  # update buy price
        #     profit = price - min_price
        #     if profit > max_profit:
        #         max_profit = profit  # update best profit

        # return max_profit

        
# time comp: O(n)
# space comp: O(1)




def main():
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print("Maximum profit:", solution.maxProfit(prices))  # 5

    prices2 = [7, 6, 4, 3, 1]
    print("Maximum profit:", solution.maxProfit(prices2))  # 0


if __name__ == "__main__":
    main()
