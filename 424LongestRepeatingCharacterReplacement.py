# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the
# string and change it to any other uppercase English character. You can perform
# this operation at most k times.
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
#
# Idea (sliding window):
#   For a window to be valid we only need to replace the characters that are NOT
#   the most frequent one. If (window size - maxFreq) > k, we can't fix the window
#   with k replacements, so we shrink it from the left.
#   maxFreq is never decreased on shrink; that's fine because the answer can only
#   grow when we later find a window with a higher maxFreq, so a stale maxFreq
#   just keeps the window from shrinking further without ever producing a wrong
#   (larger) result.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        left = 0
        maxFreq = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            maxFreq = max(maxFreq, count[s[right]])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

# Time Complexity:  O(n) - each of the right and left pointers moves forward at
#                   most n times; the max() over count is O(1) because the window
#                   update already tracks maxFreq.
# Space Complexity: O(1) - the count dict holds at most 26 uppercase letters.


def main():
    obj = Solution()

    tests = [
        (("ABAB", 2), 4),
        (("AABABBA", 1), 4),
        (("AAAA", 0), 4),
        (("ABCDE", 1), 2),
        (("A", 0), 1),
    ]

    for (s, k), expected in tests:
        result = obj.characterReplacement(s, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} characterReplacement({s!r}, {k}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()
