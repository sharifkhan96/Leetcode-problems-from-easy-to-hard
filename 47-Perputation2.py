class Solution:
    def permute(self, nums):
        nums.sort()
        result = []
        used = [False] * len(nums)



        def backtrack(path):
            # If the current path is a full permutation
            if len(path) == len(nums):
                result.append(path[:])  # make a copy
                return

            for i in range(nums):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()  # backtrack
                used[i] = False

        backtrack([])
        return result
    
# time complexity: o(n*n!), would have been n! only if we did not do the copying of path
# space complexity: o(n) because of recursion stack


# Main function
def main():
    nums = [1, 2, 3]
    solution = Solution()
    permutations = solution.permute(nums)
    print("All permutations:", permutations)


if __name__ == "__main__":
    main()
