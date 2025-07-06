from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if len(nums)== 0:
        #     return "oops, nums empty"
        # elif target == 0:
        #     return 0

        # for i in range(len(nums)):
        #     if nums[i] >= 10 ** 4:
        #         return 0
        #     if nums[i] == target:
        #         return i
        #     else:
        #         if nums[i] + 1 == target:
        #             return i + 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            

        return left
            
# complexitites:
    # time: O(log n) bcaus we are dividing the list into 2 in each iterationnnnnnnnnnnnnnnnnnnnnn
    # space; we are not using any extra space so, O(1)


def main():
    nums = [1, 3, 5, 6]
    target = 2
    obj = Solution()
    result = obj.searchInsert(nums, target)
    print(result)


if __name__ == "__main__":
    main()