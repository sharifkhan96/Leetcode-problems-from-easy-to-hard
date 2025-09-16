class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        result = 0
        for num in nums:
            result ^= num   # XOR with each number
        
        return result


def main():
    nums = [2, 2, 1]
    solution = Solution()

    print("Single number is:", solution.singleNumber(nums))

    nums2 = [4, 1, 2, 1, 2]
    print("Single number is:", solution.singleNumber(nums2))


if __name__ == "__main__":
    main()
