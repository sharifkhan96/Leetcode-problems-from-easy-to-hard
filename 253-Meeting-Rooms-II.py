import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> bool:
        # if not intervals:
        #     return 0

        # start = sorted([interval[0] for interval in intervals])
        # end = sorted([interval[1] for interval in intervals])

        # current_rooms = 0
        # max_rooms = 0
        # start_ptr, end_ptr = 0, 0

        # while start_ptr < len(intervals):
        #     if start[start_ptr] < end[end_ptr]:
        #         current_rooms += 1
        #         max_rooms = max(max_rooms, current_rooms)
        #         start_ptr += 1
        #     else:
        #         current_rooms -= 1
        #         end_ptr += 1
        # return max_rooms



        # utilizing min heap solution 
        intervals.sort(key = lambda x: x[0])
        min_heap = []

        for start, end in intervals:
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap) #min_heap

# Time complexity: O(n log n)
# Space Complexity: O(n log n)

def main():
    intervals = [[0,30],[5,10],[15,20]]
    #intervals = [[7,10],[2,4]]

    obj1 = Solution()
    print(obj1.minMeetingRooms(intervals))

if __name__ == "__main__":
    main()