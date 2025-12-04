import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)

        # Create a translation table to replace punctuation with spaces
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        # Apply the translation
        clean_text = paragraph.translate(translator)

        '''
        #completeley removing the space
        translator_remove = str.maketrans('', '', string.punctuation)
        new_text_removed = text.translate(translator_remove)
        '''

        '''
        # regex solution of removng the spaces
        import re
        words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        '''

        text_splitted = clean_text.lower().split()
        word_count = {}
        for word in text_splitted:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        return max(word_count, key=word_count.get)


        

# time comp: O(n)
# space comp: O(n)


class main():
    string1 = "hello there, how are you. you are not who are a bad person."
    banned = "you"
    obj1 = Solution()
    print(obj1.mostCommonWord(string1, banned))


if __name__ == "__main__":
    main()