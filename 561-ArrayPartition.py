class Solution:
    def arrayPairSum(self, nums)-> int:
        
        nums.sort()
        total_sum = 0

        for i in range(0, len(nums), 2):
            total_sum += nums[i]

        # same as above for loop
        '''
        for i in range(0, len(nums), 2):
            pair = (nums[i], nums[i+1])
            total_sum += min(pair)

        '''


        return total_sum


        
# time comnp:O(n) is for summation loop and o(n log n) for sorting, so: o(n log n)
# space comp: because of in place sorting , o(1)

def main():
    nums = [1,4,3,2]
    obj = Solution()
    print(obj.arrayPairSum(nums))


if __name__ == "__main__":
    main()