class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # time and space complexities: O(n) & O(1)
        left = 0
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        
        # # time and space: O(n^2) & O()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i + 1, j + 1]

        # time and space: O(n) & O(n)
        # Hashmap1 = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in Hashmap1:
        #         return [Hashmap1[diff], i + 1]
            
        #     Hashmap1[n] = i + 1





def main():
    nums = [2,7,11,15]
    target = 9
    obj1 = Solution()
    result = obj1.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()  