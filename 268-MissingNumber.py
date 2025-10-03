class Solution:
    def missingNumber(self, nums: list) -> int:
        
        lenthhhh = len(nums)
        sumofNums = lenthhhh * (lenthhhh+1) // 2
        actualSum = 0

        for num in nums:
            actualSum += num

        missingNumber = sumofNums - actualSum
        return missingNumber
    
# the above solutoiin's time & space complexitites are O(n) and O(1) respectively

''' # second way
    def missingNumber(self, nums: list) -> int:
        n = len(nums)
        xor_all = 0
        xor_nums = 0

        # XOR all numbers from 0..n
        for i in range(n + 1):
            xor_all ^= i

        # XOR all numbers in nums
        for num in nums:
            xor_nums ^= num

        # missing = difference
        return xor_all ^ xor_nums

        '''


def main():
    list1 = [3, 1, 0]
    obj = Solution()

    print(obj.missingNumber(list1))



if __name__ == "__main__":
    main()