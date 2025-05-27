class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
target = [9]




def main():
    nums = [2,7,11,15]
    target = 9
    obj1 = Solution()
    result = obj1.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()  