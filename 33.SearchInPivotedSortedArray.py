class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# complexities:
# time = O(log n) since in each iteration, we slice the array list or whatever in half. its a modified version of binary search
# space: O(1) since w ar not using any additonnal space storage aprat from some vars

def main():
    array1 = [1] #[4, 5, 6, 7, 0, 1, 2]
    target = 1
    obj = Solution()
    result = obj.search(array1, target)
    print(result)


if __name__ == "__main__":
    main()