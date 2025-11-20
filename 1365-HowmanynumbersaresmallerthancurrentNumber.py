class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        indexed_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in indexed_map:
                indexed_map[num] = i
        print(nums)
        return [indexed_map[num] for num in nums]
    # time comp: O(n log n)
    # space comp: o(n)


        '''
        # time comp: O(n^2)
        # space comp: O(n)
        # result = []
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue

        #         if nums[i] > nums[j]:
        #             count += 1
    
        #     result.append(count)
        #     count = 0
        
        # return result
        '''




class main():
    nums = [8,1,2,2,3]
    obj1 = Solution()
    result = obj1.smallerNumbersThanCurrent(nums)
    print(result)




if __name__ == "__main__":
    main()