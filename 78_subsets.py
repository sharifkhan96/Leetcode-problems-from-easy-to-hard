class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, path):
            # Add the current subset (path) to result
            result.append(path[:])
            
            # Explore further elements
            for i in range(start, len(nums)):
                # Include nums[i]
                path.append(nums[i])
                # Recurse with the next element
                backtrack(i + 1, path)
                # Backtrack (remove last element)
                path.pop()

        backtrack(0, [])
        return result


def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    solution = Solution()
    subsets_result = solution.subsets(nums)
    print("All subsets (power set):")
    print(subsets_result)


if __name__ == "__main__":
    main()
