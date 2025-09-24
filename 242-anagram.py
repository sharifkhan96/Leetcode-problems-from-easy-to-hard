class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Count character frequencies
        countS, countT = {}, {}

        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        # Compare frequency maps
        return countS == countT

'''
    Why .get(ch, 0) + 1?

dict.get(key, default) returns the value if it exists, otherwise the default.

So countS[ch] = countS.get(ch, 0) + 1 means:

If ch is already in the dictionary → increment count.

If not → start count at 1.
'''

# time comp: O(n) * O(n) => O(n)
# space comp: O(1)

def main():
    str1 = "car"
    str2 = "arc"
    solution = Solution()
    result = solution.isAnagram(str1, str2)
    print(result)


if __name__ == "__main__":
    main()