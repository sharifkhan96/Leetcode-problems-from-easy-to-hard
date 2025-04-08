class Solution:
    def findEvenNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
    

def main():
    obj1 = Solution()
    nums =  [25, 3333, 901, 22, 1771]
    result = obj1.findEvenNumbers(nums)
    print(result)

if __name__ == "__main__":
    main()