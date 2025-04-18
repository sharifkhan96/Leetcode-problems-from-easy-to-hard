class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        for num in nums:
            index = abs(num) -1
            if nums[index] > 0:
                nums[index] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result



def main():
    nums = [1,1,2,1,1,1,8,3] #[4,3,2,7,8,2,3,1]
    print("Initial nums: ", nums)
    obj1 = Solution()
    result = obj1.findDisappearedNumbers(nums)
    print("Resulting disappeared numbers: ",result)

if __name__ == "__main__":
    main()