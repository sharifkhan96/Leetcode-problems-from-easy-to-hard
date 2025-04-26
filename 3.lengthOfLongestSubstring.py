# Given a string s, find the length of the longest substring without duplicate characters.
# for reference, go to the leetdcode problem of lengthOfLongestSubstring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 # start of current window
        max_lenght = 0

        for right in range(len(s)):
            # right is the current char
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_lenght = max(max_lenght, right - left + 1)
        return max_lenght

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         maxLength = 0
#         charSet = set()
#         left = 0
        
#         for right in range(n):
#             if s[right] not in charSet:
#                 charSet.add(s[right])
#                 maxLength = max(maxLength, right - left + 1)
#             else:
#                 while s[right] in charSet:
#                     charSet.remove(s[left])
#                     left += 1
#                 charSet.add(s[right])
        
#         return maxLength

def main():
    string = "aba"
    obj = Solution()
    result = obj.lengthOfLongestSubstring(string)
    print(result)


if __name__ == "__main__":
    main()