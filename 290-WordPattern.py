class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                if w in word_to_char:
                    return False
                char_to_word[c] = w
                word_to_char[w] = c
        
        return True
    


# time complexity: o(n)
# space comp: o(n)


def main():
    pattern = 'abba'
    word = "sharif cat cat sharif"
    word1 = "sharif cat cat cat"
    obj1 = Solution()
    print(pattern, " : ", word, " --> ", obj1.wordPattern(pattern, word))
    print(pattern, " : ", word1, " --> ", obj1.wordPattern(pattern, word))


if __name__ == "__main__":
    main()
