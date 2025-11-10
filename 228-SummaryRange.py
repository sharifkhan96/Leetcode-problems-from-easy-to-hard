class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            #  if it's the end of a continuous range
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                # if therange has only one element
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                # startingggggggggggggggg new range
                if i < len(nums):
                    start = nums[i]

        return result
    
# time comp: O(n)
# space comp: O(1)


def main():
    nums = [0,1,2,4,5,7]
    obj = Solution()
    print(obj.summaryRanges(nums))  


if __name__ == "__main__":
    main()
