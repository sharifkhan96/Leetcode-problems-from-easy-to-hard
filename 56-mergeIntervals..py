class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

# o(n log n) & O(log n) or O(n)
        
        
def main():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    ob = Solution()
    print(ob.merge(intervals))


if __name__ == "__main__":
    main()