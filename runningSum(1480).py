class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        new_array = []
        current_sum = 0
        for num in nums:
            current_sum += num
            new_array.append(current_sum)

        return new_array



def main():

    nums = [1, 3, 4, 6]
    obj1 = Solution()

    result = obj1.runningSum(nums)
    print(f"The running sum of the {nums} array is: {result}")



if __name__ == "__main__":
    main()