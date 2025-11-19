class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        #nums.sort()
        result = []
        count = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)-1):
                if nums[i] > nums[j]:
                    count += 1
                else:
                    continue
            result.append(count)
        
        return result


# time comp: O(m*n)
# space comp: O(n)


class main():
    nums = [8,1,2,2,3]
    obj1 = Solution()
    result = obj1.smallerNumbersThanCurrent(nums)
    print(result)




if __name__ == "__main__":
    main()