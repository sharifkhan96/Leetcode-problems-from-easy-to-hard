# Given a string s, find the length of the longest substring without duplicate characters.
# for reference, go to the leetdcode problem of lengthOfLongestSubstring

class Solution:
    def longestPalindromeSubstring(self, givenString: str) -> str:
        palindrom = "" # used for the reutnring of the actual palindrom
        for start in range(len(givenString)): # check for the start of the palindrom
            for end in range(start, len(givenString)): # check for the end of the palindrom from start-end in each iteration
                if givenString[start : end + 1] == givenString[start : end + 1][::-1]: # checking if an actual string matches with its inverse form
                    if len(givenString[start : end + 1]) > len(palindrom): # if it does, then check if the new palindrom is greater in size than the previous updated palidnrom
                        palindrom = givenString[start : end + 1]

        return palindrom  # return the shitttttttttt :-)

def main():
    string = "babad"
    obj = Solution()
    result = obj.longestPalindromeSubstring(string)
    print(result)


if __name__ == "__main__":
    main()