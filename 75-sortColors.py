class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# time & space complexities:
# O(n)
# o(1)


def main():
    nums = [2,0,2,1,1,0]
    print(nums)
    obj = Solution()
    obj.sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()