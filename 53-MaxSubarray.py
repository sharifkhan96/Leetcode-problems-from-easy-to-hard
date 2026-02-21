class Solution:
    def maxSubArray(self, nums: list[int]) -> int:


        # dp solution:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], dp[i-1] + nums[i])

        # return max(dp)


        # kadan's algo: time and space complexities: O(n) & O(1)
        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
                currentSum = max(nums[i], currentSum + nums[i])
                maxSum = max(currentSum, maxSum)

        return maxSum


        
        # maxSum = nums[0]
        # currentSum = 0
        # start = 0
        # best_start = 0
        # best_end = 0

        # for i, n in enumerate(nums):
        #     if currentSum < 0:
        #         currentSum = 0
        #         start = i

        #     currentSum += n

        #     if currentSum > maxSum:
        #         maxSum = currentSum
        #         best_start = start
        #         best_end = i
        # return maxSum, (best_start, best_end)
# time comp: O(n)
# space comp: O(n)
    


class main():
    abc = [-2,1,-3,4,-1,2,1,-5,4]
    
    obj1 = Solution()
    print(obj1.maxSubArray(abc))




if __name__ == "__main__":
    main()