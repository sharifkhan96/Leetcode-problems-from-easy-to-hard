from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []

        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap, x)

        return heap[0]


def main() -> None:
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    sol = Solution()
    result = sol.findKthLargest(nums, k)

    print(f"The {k}th largest element is: {result}")


if __name__ == "__main__":
    main()
