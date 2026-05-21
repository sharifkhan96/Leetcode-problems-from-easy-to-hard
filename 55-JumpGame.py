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
    
    # Greedy solution: works way backward...
    def canJumpGreedy(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
    

# time comp: O(N)
# space comp: O(1)

class main():
    nums = [2,3,1,1,4]   
    obj1 = Solution()
    #print(obj1.canJump(nums))
    print(obj1.canJumpGreedy(nums))




if __name__ == "__main__":
    main()