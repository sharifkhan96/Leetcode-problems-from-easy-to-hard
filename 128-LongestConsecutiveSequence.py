class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # brute force method: O(n3) & O(1)
        # longest_streak = 0

        # for num in nums:
        #     current_num = num
        #     current_streak = 1

        #     while current_num + 1 in nums:
        #         current_num += 1
        #         current_streak += 1

        #     longest_streak = max(longest_streak, current_streak)

        # return longest_streak


        # o(n log n)
        # if not nums:
        #     return 
        
        # nums.sort()
        # longest_streak = 1
        # current_streak = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         if nums[i] == nums[i - 1] + 1:
        #             current_streak += 1
        #         else:
        #             longest_streak = max(longest_streak, current_streak)
        #             current_streak = 1


        # return max(longest_streak, current_streak)



        # o(n)
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


        


class main():

    nums = [100,5,200,1,3,2]
    obj1 = Solution()
    result = obj1.longestConsecutive(nums)
    print(result)




if __name__ == "__main__":
    main()