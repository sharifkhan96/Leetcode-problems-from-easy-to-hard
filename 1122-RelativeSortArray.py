from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # step 1: count frequency of each element in arr1
        freq = {}
        for item in arr1:
            freq[item] = freq.get(item, 0) + 1
        #freq = Counter(arr1)
        
        result = []

        # step2: add elements following arr2’s order
        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]

        # step 3: add remaining elements ( not in arr2)
        for num in sorted(freq.keys()):
            result.extend([num] * freq[num])

        return result


# time complexity: O(n log n)  (because of sorting the leftovers)
# space complexity: O(n)

def main():
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    obj = Solution()
    print(obj.relativeSortArray(arr1, arr2))


if __name__ == "__main__":
    main()
