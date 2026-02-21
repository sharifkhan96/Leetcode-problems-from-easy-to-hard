class Solution:
    def productExceptSelf(self, nums):
        # n = len(nums)
        # answer = [1] * n

        # # Step 1: Left products
        # for i in range(1, n):
        #     answer[i] = answer[i - 1] * nums[i - 1]

        # # Step 2: Right products
        # right_product = 1
        # for i in range(n - 1, -1, -1):
        #     answer[i] *= right_product
        #     right_product *= nums[i]

        # return answer


        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



def main():
    nums = [1, 2, 3, 4]
    obj = Solution()
    print(obj.productExceptSelf(nums))


if __name__ == "__main__":
    main()
