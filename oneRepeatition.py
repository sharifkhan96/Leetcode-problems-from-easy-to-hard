class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0 
        current_count = 0
        for i in nums:
            if i == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0                
            
        return max_count
    

def main():
    obj1 = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    result = obj1.findMaxConsecutiveOnes(nums)
    print(result)

if __name__ == "__main__":
    main()