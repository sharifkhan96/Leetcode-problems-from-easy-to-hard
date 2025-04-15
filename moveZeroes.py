class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # extra space: time comp = o(n), space comp = o(n)
        nums2 = []
        for i in nums:
            if i != 0:
                nums2.append(i)
                
        count_zero = len(nums) - len(nums2)
        nums2.extend([0] * count_zero)

        return nums, nums2

        # optimized: time comp = o(n), space comp = o(1)
        # extra_zeroes_position = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[extra_zeroes_position] = nums[i]
        #         extra_zeroes_position +1 

        # for i in range(extra_zeroes_position, len(nums)):
        #     nums[i] = 0
        # return nums



def main():
    
    nums = [0,1,0,3,12]
    obj1 = Solution()
    result1, result2 = obj1.moveZeroes(nums)
    print(result1)
    print(result2)
    # result3 = obj1.moveZeroes(nums)
    # print(result3)



if __name__ == "__main__":
    main()