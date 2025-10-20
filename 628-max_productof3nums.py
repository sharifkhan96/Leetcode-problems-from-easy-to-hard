class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        # casse 1: top three largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
      
        # case 2: two smallest+ largest
        case2 = nums[0] * nums[1] * nums[-1]
      
        return max(case1, case2)


# sorting: O(n log n)
# time comp: O(1)

def main():
    nums = [1, 2, 3]
    obj = Solution()
    print(obj.maximumProduct(nums))  # Output: 6


if __name__ == "__main__":
    main()
