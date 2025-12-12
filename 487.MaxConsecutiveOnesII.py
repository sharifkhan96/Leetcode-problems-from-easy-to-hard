class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        return max_len

# time comp: O(n)
# space comp: O(1)
# statement: finding the max num of ones if we can flip max 1 zero into one.


def main():
    nums = [1,0,1,1,0] # output shall be 4 since we can flip second zero into 1 and 1s become four ones
    obj = Solution()
    print(obj.findMaxConsecutiveOnes(nums))


if __name__ == "__main__":
    main()