class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for char in s:
            if char != " ":
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)
        
        return " ".join(reversed(words))


# time comp: O(n)
# space comp; O(n)

def main():
    string1 = "hello world, i wanna go the extra mile"
    obj1 = Solution()
    print(obj1.reverseWords(string1))



if __name__ == "__main__":
    main()