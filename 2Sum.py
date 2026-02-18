class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # O(n)
        Hashmap1 = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hashmap1:
                return [Hashmap1[diff], i]
            
            Hashmap1[n] = i





def main():
    nums = [2,7,11,15]
    target = 18
    obj1 = Solution()
    result = obj1.twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()  