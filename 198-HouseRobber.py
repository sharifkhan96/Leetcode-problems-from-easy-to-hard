class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n-1]

        
#time comnp:O(n)
#space comp: o(n)

'''
space comp of o(1)
        prev1, prev2 = 0, 0

        for num in nums:
            temp = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = temp
        
        return prev1
'''

def main():
    nums = [1,2,3,1]
    obj = Solution()
    print(obj.rob(nums))


if __name__ == "__main__":
    main()