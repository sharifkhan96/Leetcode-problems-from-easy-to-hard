class Solution:
    
    # used for recursion+memoization solution
    def __init__(self):
        self.memo = {}


    # recursion + memoization
    def rob(self, nums: list[int]) -> int:
        self.memo = {}

        return self.robFrom(0, nums)
    
    def robFrom(self, index, nums):
        # base case
        if index >= len(nums):
            return 0
        
        # return cached values
        if index in self.memo:
            return self.memo[index]
        
        # actual recursion
        ans = max(
                    self.robFrom(index + 1, nums), self.robFrom(index + 2, nums) + nums[index]
                  
                  )
        # cache for future use
        self.memo[index] = ans
        return ans
        
    
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
    #         dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    #     return dp[n-1]

        
#time comnp:O(n)
#space comp: o(n)

'''
space comp of o(1)
        prev1, prev2 = 0, 0

        for num in nums:
            temp = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = temp
        
        return prev2
'''

def main():
    nums = [1,2,3,1]
    obj = Solution()
    print(obj.rob(nums))


if __name__ == "__main__":
    main()