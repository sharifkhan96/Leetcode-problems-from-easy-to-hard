class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # algo
        # sort the intervals
        intervals.sort(key=lambda x: x[0])
        
        # travers =
        for i in range(len(intervals)-1):
            # if end of ith index value is less than or eq to # # start of ith+1 index value: no overlap, cont till # end: true

            if intervals[i][1] <= intervals[i+1][0]:
                continue
            else:
                return False

        # otherwise overlap, return false
        return True

        # def overlap(interval1: List[int], interval2: List[int]) -> bool:
        #     return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
        #         or interval2[0] >= interval1[0] and interval2[0] < interval1[1])

        # for i in range(len(intervals)):
        #     for j in range(i + 1, len(intervals)):
        #         if overlap(intervals[i], intervals[j]):
        #             return False
        # return True



# Time complexity: O(n log n)
# Space Complexity: O(n log n)

def main():
    intervals = [[0,30],[5,10],[15,20]]
    

    obj1 = Solution()
    print(obj1.canAttendMeetings(intervals))

if __name__ == "__main__":
    main()