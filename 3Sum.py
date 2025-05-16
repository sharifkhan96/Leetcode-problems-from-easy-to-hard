class Solution:
    def threeSum(self, nums: list[int]) -> str:
        
        nums = sorted(nums)

        i = 0
        triplets = []

        # here, we wanna avoid the duplicates
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

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
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
 
        return triplets  

# the time and space complexities are:
# time:  because the loops only runs constant times in this case, 13 times
# space:  we have not used any additional space


def main():
    array1 = [-1, 0, 1, 2, -1, -4]
    obj1 = Solution()
    result = obj1.threeSum(array1)
    print(result)

if __name__ == "__main__":
    main()