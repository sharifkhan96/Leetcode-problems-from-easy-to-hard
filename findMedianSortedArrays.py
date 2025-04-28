# Given a string s, find the length of the longest substring without duplicate characters.
# for reference, go to the leetdcode problem of lengthOfLongestSubstring

class Solution:
    def findMedianSortedArrays(self, arr1: list[int], arr2: list[int]) -> float:
        
        # merged = arr1 + arr2
        # merged.sort()
        # return merged

        # first way: o(n log n)
        # merged = arr1 + arr2
        # merged.sort()
        # n = len(merged)
        # if n % 2 == 1:
        #     median = merged[n // 2]
        # else:
        #     median = (merged[n // 2 - 1] + merged[n // 2]) / 2

        # return median
        

        # second way: o(n)
        p1 = 0
        p2 = 0
        merged = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                merged.append(arr1[p1])
                p1 += 1
            else:
                merged.append(arr2[p2])
                p2 += 1 
 
        while p1 < len(arr1):
            merged.append(arr1[p1])
            p1 += 1
        
        while p2 < len(arr2):
            merged.append(arr2[p2])
            p2 += 1
        
        n = len(merged)
        if n % 2 == 1:
            median = merged[n // 2]
        else:
            median = (merged[n // 2 -1 ] + merged[n // 2]) / 2


        return median



def main():
    array1 = [1,3]
    array2 = [2]
    obj = Solution()
    result = obj.findMedianSortedArrays(array1, array2)
    print(result)
    

if __name__ == "__main__":
    main()