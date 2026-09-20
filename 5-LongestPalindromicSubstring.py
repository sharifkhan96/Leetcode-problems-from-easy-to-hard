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
        #return "heheh"
        n = len(string)

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_length = 1

        for right in range(n):
            for left in range(right + 1):

                # check if left & right are equal
                if string[left] == string[right]:

                    # len is either 1 or 2 or 3
                    if right - left <= 2:
                        dp[left][right] = True
                    # inc left & dec right
                    else:
                        dp[left][right] = dp[left + 1][right - 1]
                
                # update longest palidnrom
                if dp[left][right]:
                    length = right - left + 1

                if length > max_length:
                    max_length = length
                    start = left

        return string[start: start+max_length]

    # time complexity: O(n^2)
    # space complexity: O(n^2)


def main():
    string1 = "madasa"
    obj = Solution()
    result = obj.longestPalindrome(string1)
    print(result)


if __name__ == "__main__":
    main()