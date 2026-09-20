class Solution:
    def longestPalindrome(self, string: str) -> str:
        # bruteforce solution
        '''
        self.string = string
                for length in range(len(string), 0, -1):
                    for start in range(len(string) - length + 1):
                        if self.checkPalindrom(start, start+length):
                            return string[start : start+length]
        
                return ""
        
        
            def checkPalindrom(self, i, j) -> bool:
                left = i
                right = j - 1
        
                while left < right:
                    if self.string[left].lower() != self.string[right].lower():
                        return False
        
                    left += 1
                    right -= 1
                return True
        # time complexity: O(n^3)
        # space complexity: O(1)
        '''

        # dp solution
        return "heheh"


def main():
    string1 = "madasa"
    obj = Solution()
    result = obj.longestPalindrome(string1)
    print(result)


if __name__ == "__main__":
    main()