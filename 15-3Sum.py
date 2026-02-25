class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums = sorted(nums)

        i = 0
        triplets = []

        for i in range(len(nums)):
            # here, we wanna avoid the duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1
            # core logic 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # avoiding the duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                   # avoiding the duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
 
        return triplets  

# the time and space complexities are:
# time:  O(n^2)
# space:  O(1) or O(n) bcos of sorting


def main():
    array1 = [-1, 0, 1, 2, -1, -4]
    obj1 = Solution()
    result = obj1.threeSum(array1)
    print(result)

if __name__ == "__main__":
    main()