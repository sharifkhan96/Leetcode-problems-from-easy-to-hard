class Solution:
    def maxSubArray(self, nums: list[int]) -> int:


        # dp sol:
        # dp = [0] * len(nums)
        # #return dp
        # dp[0] = nums[0]

        # for i, n in enumerate(nums):
        #     dp[i] = max(n, dp[i-1]+n)

        # return max(dp)


        
        maxSum = nums[0]
        currentSum = 0
        start = 0
        best_start = 0
        best_end = 0

        for i, n in enumerate(nums):
            if currentSum < 0:
                currentSum = 0
                start = i

            currentSum += n
            if currentSum > maxSum:
                maxSum = currentSum
                best_start = start
                best_end = i
            maxSum = max(maxSum, currentSum)
        return maxSum, (best_start, best_end)
# time comp: O(n)
# space comp: O(n)
    


class main():
    abc = [-2,1,-3,4,-1,2,1,-5,4]
    
    obj1 = Solution()
    print(obj1.maxSubArray(abc))




if __name__ == "__main__":
    main()