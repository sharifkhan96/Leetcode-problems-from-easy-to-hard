class Solution:
    
    # def rob(self, nums: list[int]) -> int:
        
    #     def get_max(nums):
    #         prev_rob = max_rob = 0

    #         for cur_val in nums:
    #             temp = max(max_rob, prev_rob + cur_val)
    #             prev_rob = max_rob
    #             max_rob = temp
    #         return max_rob

    #     return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])
    
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robMax(nums[:-1]), self.robMax(nums[1:]))
    
    def robMax(self, nums: list[int]) -> int:
        t1 = t2 = 0
        for current in nums:
            temp = max(t2, t1 + current)
            t1 = t2
            t2 = temp

        return t2

        
#time comnp:O(n)
#space comp: o(n)



def main():
    nums = nums = [2,3,2]
    obj = Solution()
    print(obj.rob(nums))


if __name__ == "__main__":
    main()