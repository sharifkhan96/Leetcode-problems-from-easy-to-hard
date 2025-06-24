class Solution:
    def strSTR(self, haystack: str, needle: str) -> int:
        print("lets see if needle is in haystack or not. . .")
        needleLength = len(needle)
        haystackLength = len(haystack)

        # edge cases
        if needleLength > haystackLength:
            return -1
        elif needleLength == 0:
            return 0
        # elif needle == haystack:
        #     return 0
        # elif needleLength > 10**4:
        #     return -1

        # the crux of ht e algorith for this problem is the in the for loop + if statement
        # time complexity: O(m*n)
        # we can have time comp of O(m+n) when we use KMP algo
        for i in range(haystackLength - needleLength + 1):
            if haystack[i:i + needleLength] == needle:
                return i      
        
        return -1


def main():
    haystack = "leetcode"
    needle = "leeto"
    obj1 = Solution()
    result = obj1.strSTR(haystack, needle)
    print(result)



if __name__ == "__main__":
    main()