class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        def overlap(interval1: list[int], interval2: list[int]) -> bool:
            return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
                or interval2[0] >= interval1[0] and interval2[0] < interval1[1])

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True





# Time complexity: O(n^2)
# Space Complexity: O(1)

def main():
    intervals = [[0,30],[5,10],[15,20]]
    

    obj1 = Solution()
    print(obj1.canAttendMeetings(intervals))

if __name__ == "__main__":
    main()