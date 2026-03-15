class Solution:
    
    # used for recursion+memoization solution
    def __init__(self):
        self.memo = {}


    # recursion + memoization
    # def rob(self, nums: list[int]) -> int:
    #     self.memo = {}

    #     return self.robFrom(0, nums)
    
    # def robFrom(self, index, nums):
    #     # base case
    #     if index >= len(nums):
    #         return 0
        
    #     # return cached values
    #     if index in self.memo:
    #         return self.memo[index]
        
    #     # actual recursion
    #     ans = max(
    #                 self.robFrom(index + 1, nums), self.robFrom(index + 2, nums) + nums[index]
                  
    #               )
    #     # cache for future use
    #     self.memo[index] = ans
    #     return ans
        

    # dp1
    # def rob(self, nums: list[int]) -> int:
    #     n = len(nums)

    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return nums[0]
        
    #     dp = [0] * n
    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0], nums[1])

    #     for i in range(2, n):
    #         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    #     return dp[n-1]
    

    # dp2
    # def rob(self, nums: list[int]) -> int:
    #     if not nums:
    #         return 0
        
    #     maxRobbedAmount = [None for _ in range(len(nums) + 1)]

    #     n = len(nums)

    #     maxRobbedAmount[n], maxRobbedAmount[n - 1] = 0, nums[n - 1]

    #     for i in range(n - 2, -1, -1):
    #         maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

    #     return maxRobbedAmount[0]
    
    # dp3: space optimized ;)
    def rob(self, nums: list[int]) -> int:
    
        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next
        
#time comnp:O(n)
#space comp: o(n)


        # space complexity o(1)
        # prev1, prev2 = 0, 0

        # for num in nums:
        #     temp = max(prev1 + num, prev2)
        #     prev1 = prev2
        #     prev2 = temp
        
        # return prev2


def main():
    nums = [1,2,3,1]
    obj = Solution()
    print(obj.rob(nums))


if __name__ == "__main__":
    main()