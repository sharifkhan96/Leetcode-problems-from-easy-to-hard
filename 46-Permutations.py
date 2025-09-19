class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path):
            # If the current path is a full permutation
            if len(path) == len(nums):
                result.append(path[:])  # make a copy
                return

            for num in nums:
                if num in path:  # skip if already used
                    continue
                path.append(num)
                backtrack(path)
                path.pop()  # backtrack

        backtrack([])
        return result


# Main function
def main():
    nums = [1, 2, 3]
    solution = Solution()
    permutations = solution.permute(nums)
    print("All permutations:", permutations)


if __name__ == "__main__":
    main()
