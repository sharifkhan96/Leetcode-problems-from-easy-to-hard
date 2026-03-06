
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # n = len(nums)
        # dp = [1] * n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)


        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)


# tiem and space complexities: O(n^2) & O(n)

def main():
    nums = [10,9,2,5,3,7,101,18]

    obj1 = Solution()
    print(obj1.lengthOfLIS(nums))


if __name__ == "__main__":
    main()