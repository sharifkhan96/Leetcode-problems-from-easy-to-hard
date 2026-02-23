from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]
        
    
        while right > left:
            
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        


# time and space complexities:
# O(log n) and O(1)


class main():
    
    nums = [3,4,5,1,2]
    obj1 = Solution()
    print(obj1.findMin(nums=nums))




if __name__ == "__main__":
    main()