class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # step1 : plcaing each number in its correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] -1] != nums[i]:
                nums[i], nums[nums[i] -1] = nums[nums[i]-1], nums[i]


        # step 2: finding the first index where nums[i] != i+1:
        for i in range(n):
            if nums[i] != i +1 :
                return i + 1 

        return n + 1 

        
#time comnp:O(n)
#space comp: o(1)

def main():
    nums = [3, 4, -1, 1]
    obj = Solution()
    print(obj.firstMissingPositive(nums))


if __name__ == "__main__":
    main()