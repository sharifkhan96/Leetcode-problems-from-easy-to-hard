class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")
        new_string = list(s)
        left, right = 0, len(new_string) - 1

        while left < right:
            if new_string[left] not in vowels:
                left += 1
            elif new_string[right] not in vowels:
                right -= 1
            else:
                new_string[left], new_string[right] = new_string[right], new_string[left]
                left += 1
                right -= 1
        
        return "".join(new_string)

# Time complexity: O(n) 
# Space complexity: O(n)


    
def main():
    string1 = input("Enter your string: ")
    obj = Solution()
    print("String with reversed vowels: ", obj.reverseVowels(string1))


if __name__ == "__main__":
    main()