class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
       ''''
       # O(n^3)
       closest_sum = float('inf')
       for i in range(len(nums) - 2):
           for j in range(i + 1, len(nums) - 1):
               for k in range(j + 1, len(nums)):
                   current_sum = nums[i] + nums[j] + nums[k]
                   if abs(current_sum - target) < abs(closest_sum - target):
                       closest_sum = current_sum
       return closest_sum
       '''
       # O(n^2)
       nums.sort()
       closest_sum = float('inf')
       for i in range(len(nums) - 2):
         left = i + 1
         right = len(nums) - 1
         while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest_sum):
                closest_sum = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
       return closest_sum

       




def main():
    array1 = [-1,2,1,-4]
    target = 1
    obj1 = Solution()
    result = obj1.threeSumClosest(array1, target)
    print(result)

if __name__ == "__main__":
    main()