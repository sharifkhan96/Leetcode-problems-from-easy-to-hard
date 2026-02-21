class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Step 1: Left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Step 2: Right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


        #----------------two pass prefix and postfixes solutions
        # res = [1] * len(nums)

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # return res
    
    #----------------arrays of prefix and postfixes solution-------------
        # n = len(nums)
        # prefix = [1] * n
        # postfix = [1] * n
        # res = [1] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]

        # for i in range(n - 2, -1, -1):
        #     postfix[i] = postfix[i + 1] * nums[i + 1]

        # for i in range(n):
        #     res[i] = prefix[i] * postfix[i] 

        # return res




    #-------------------brute force solution------------------------
        n = len(nums)
        res = [1] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            res[i] = prod
        
        return res




def main():
    nums = [1, 2, 3, 4]
    obj = Solution()
    print(obj.productExceptSelf(nums))


if __name__ == "__main__":
    main()
