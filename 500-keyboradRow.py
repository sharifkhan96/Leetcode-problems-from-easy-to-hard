class Solution:
    def findWords(self, words):
        # define sets for each keyboard row
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            # cnvert word to lowercase and make it a set of characters
            lowercase_set = set(word.lower())

            # check if the entire set of letters belongs to one keyboard row
            if lowercase_set <= row1 or lowercase_set <= row2 or lowercase_set <= row3:
                result.append(word)

        return result

# time complexity: O(n * m)
# space complexity: O(1)

# examplee usage
def main():
    words = ["Hello", "Alaska", "Dad", "Peace"]
    obj = Solution()
    print(obj.findWords(words)) 


if __name__ == "__main__":
    main()
