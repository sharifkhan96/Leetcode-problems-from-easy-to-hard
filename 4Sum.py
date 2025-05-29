class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums = sorted(nums)
        i = 0
        quadruplets = []

        for i in range(len(nums) - 3):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] +  nums[left] +  nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                
        return quadruplets  

# the time and space complexities are:
# time: O(n^3)
# space: O(1) considering not the output list quadruplets


def main():
    array1 = [1, 0, -1, 0, -2, 2]
    target = 0
    obj1 = Solution()
    result = obj1.fourSum(array1, target)
    print(result)

if __name__ == "__main__":
    main()