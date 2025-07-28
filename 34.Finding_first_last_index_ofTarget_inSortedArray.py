
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
       first = self.findFirst(nums, target) # here, we basically find the first index position of the given targt
       last = self.findLast(nums, target)   # while here, we try to find the last index postion of hte the given target.
       
       return [first, last] 


    # function for fidning the 1st postion of given target
    def findFirst(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return result 
    

    # function for fidning the last postion of given target
    def findLast(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return result


# time comp: o(log n)
# spac3 comp: o(1)

def main():
    array1 = [5, 7, 7, 8, 8, 10]
    target = 7
    obj = Solution()
    result = obj.searchRange(array1, target)
    print(result)


if __name__ == "__main__":
    main()