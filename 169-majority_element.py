class Solution:
    def majorityElement(self, nums):

        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count +=(1 if num == candidate else -1)
        
        return candidate

# time & space complexities:
# O(n) space
# O(1) time

def main():
    nums = list(map(int, input("Enter numbers separated by space:  ").split()))
    solution = Solution()
    print("Majority element :", solution.majorityElement(nums))


if __name__ == "__main__":
    main()
