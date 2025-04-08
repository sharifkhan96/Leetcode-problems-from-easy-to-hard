
"""_summary_

    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105

ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        
        # Count characters in the magazine
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        # Check if ransomNote can be constructed
        for c in ransomNote:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        
        return True
"""

# also working: 

class Solution:
    def canConstruct(self, ransomeNote: str, magazine: str) -> bool:
        for i in ransomeNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i, "" , 1)
        return True


def main():
    ransomeNote = str(input("Enter the ransomeNOte: ").lower())
    magazine = str(input("Enter the magazine: ").lower())

    obj1 = Solution()
    result = obj1.canConstruct(ransomeNote, magazine)

    print(f"It is {result} that {ransomeNote} can be constructed from {magazine}.")


if __name__ == "__main__":
    main()