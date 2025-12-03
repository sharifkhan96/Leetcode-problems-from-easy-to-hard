import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        lower_paragraph = paragraph.lower()
        # Create a translation table to replace punctuation with spaces
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        # Apply the translation
        new_text = lower_paragraph.translate(translator)
        #print(new_text)

        '''
        translator_remove = str.maketrans('', '', string.punctuation)
        new_text_removed = text.translate(translator_remove)
        '''

        '''
        # regex solution of removng the spaces
        import re

        text = "Hello, world! How are you?"
        # Replace all non-word characters (including punctuation) with a space
        new_text = re.sub(r'[^\w\s]', ' ', text)
        print(new_text)

        # Replace all punctuation with an empty string (remove them)
        new_text_removed = re.sub(r'[^\w\s]', '', text)
        print(new_text_removed)
        '''
        new_text = new_text.replace(banned, '')
        new_text_splitted = new_text.split()
        word_count = {}
        for word in new_text_splitted:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return max(word_count)


        

# time comp: O(n)
# space comp: O(n)


class main():
    abc = "hello there, how are you. you are not who are a bad person."
    banned = "you"
    obj1 = Solution()
    print(obj1.mostCommonWord(abc, banned))




if __name__ == "__main__":
    main()