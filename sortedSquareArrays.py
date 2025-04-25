class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # result = []
        # for i in nums:
        #     result.append(i * i)
            
        # return sorted(result)
        length = len(nums)
        left = nums[0]
        right = length - 1
        result = [0] * length
        position = length - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] ** 2
                left += 1
            else:
                result[position] = nums[right] ** 2
                right -= 1
            position -= 1
        return sorted(result)


def main():
    obj1 = Solution()
    nums =  [-4,-1,0,3,10]
    result = obj1.sortedSquares(nums)
    print(result)

if __name__ == "__main__":
    main()