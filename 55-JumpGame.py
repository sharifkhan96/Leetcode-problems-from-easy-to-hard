class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True

        return True
    

# time comp: O(N)
# space comp: O(1)

class main():
    nums = [2,3,1,1,4]   
    obj1 = Solution()
    print(obj1.canJump(nums))



if __name__ == "__main__":
    main()