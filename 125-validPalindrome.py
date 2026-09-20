class Solution:
    def isPalindrome(self, s: str) -> bool:

        # the most raw/pure way ;;)
        left, right = 0, len(s) -1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


    def isAlphaNum(self, char):
        return  (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
    
        
        '''
        # the most intuitive way
        left, right = 0, len(s) - 1
        
                while left < right:
                    
                    while left < right and not s[left].isalnum():
                        left += 1
        
                    while left < right and not s[right].isalnum():
                        right -= 1
        
                    if s[left].lower() != s[right].lower():
                        return False
                    
                    left += 1
                    right -= 1
        
                return True
        # time complexity: O(n)
        # space complexity: O(1)
        '''


        '''
        # shortest way
        newString = ""

        for char in s:
            if char.isalnum():
                newString += char.lower()
        return newString == newString[::-1]
        '''
# time complexity: O(n)
# space complexity: O(n)

def main():
    string1 = "madam"
    obj = Solution()
    result = obj.isPalindrome(string1)
    print(result)


if __name__ == "__main__":
    main()