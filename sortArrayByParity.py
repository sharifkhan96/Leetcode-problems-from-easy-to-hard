class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        checker = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[checker] = nums[checker],  nums[i]
                checker += 1
        return nums




def main():
    
    nums = [3,1,2,4]
    obj1 = Solution()
    result1 = obj1.sortArrayByParity(nums)
    print(result1)



if __name__ == "__main__":
    main()