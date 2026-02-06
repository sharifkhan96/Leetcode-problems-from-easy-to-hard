from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # # Step 1: Count frequencies
        # freq = Counter(nums)  # e.g. Counter({1:3, 2:2, 3:1})
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Step 2: Use a heap to get top k frequent elements
        return heapq.nlargest(k, freq.keys(), key=freq.get)

# time complexity: O(n log k) where n is for counting and log k for heap operations
# space complexity: O(n + k) where n is for freq map and k is for heap



def main():
    nums = [1, 2, 1, 2, 3, 1]
    k = 2

    obj = Solution()
    print(obj.topKFrequent(nums, k))  


if __name__ == "__main__":
    main()