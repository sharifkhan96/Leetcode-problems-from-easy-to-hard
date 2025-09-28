class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]
            
            # Move pointers
            left += 1
            right -= 1


# time complexity: O(n)
# space complexity: O(1)


def main():
    string1 = ["s", "h", "a", "r", "i", "f"]
    obj = Solution()
    result = obj.reverseString(string1)
    print("Reversed string: ", "".join(string1))
    print("Reversed list: ", string1)


if __name__ == "__main__":
    main()