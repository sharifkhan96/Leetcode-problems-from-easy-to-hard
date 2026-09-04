# 76. Minimum Window Substring
# Hard
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty
# string "".
# The testcases will be generated such that the answer is unique.
#
# Idea (sliding window):
#   Count how many of each character t needs. Expand the window with `right`,
#   and whenever a character's count drops to exactly what's needed, mark one
#   more "requirement satisfied". Once all requirements are satisfied, shrink
#   the window from the left as far as possible while still valid, recording
#   the smallest valid window seen. Then keep expanding.

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)  # total chars still needed (with multiplicity)

        left = 0
        bestLen = float("inf")
        bestLeft = 0

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                if right - left + 1 < bestLen:
                    bestLen = right - left + 1
                    bestLeft = left

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if bestLen == float("inf") else s[bestLeft:bestLeft + bestLen]

# Time Complexity:  O(m + n) - building `need` from t is O(n); the right and left
#                   pointers over s each move forward at most m times.
# Space Complexity: O(n) - `need` holds at most the distinct characters in t
#                   (bounded by the alphabet size, so O(1) for a fixed charset).


def main():
    obj = Solution()

    tests = [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "a"), "a"),
        (("a", "aa"), ""),
        (("", "a"), ""),
        (("aa", "aa"), "aa"),
    ]

    for (s, t), expected in tests:
        result = obj.minWindow(s, t)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} minWindow({s!r}, {t!r}) = {result!r} (expected {expected!r})")


if __name__ == "__main__":
    main()
