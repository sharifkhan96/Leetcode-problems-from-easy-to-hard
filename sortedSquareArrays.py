class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            result.append(i * i)
            
        return sorted(result)
    
def main():
    obj1 = Solution()
    nums =  [-4,-1,0,3,10]
    result = obj1.sortedSquares(nums)
    print(result)

if __name__ == "__main__":
    main()