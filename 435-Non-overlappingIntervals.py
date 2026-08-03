class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])

        ans = 0

        recentEndTime = float('-inf')

        for startTime, endTime in intervals:
            if startTime >= recentEndTime:
                recentEndTime = endTime
            else:
                ans += 1

        return ans


# Time complexity: O(n⋅logn)
# Space Complexity: O(logn) or O(n)

def main():
    intervals = [[1,2],[2,3],[3,4],[1,3]]


    obj1 = Solution()
    print(obj1.eraseOverlapIntervals(intervals))

if __name__ == "__main__":
    main()