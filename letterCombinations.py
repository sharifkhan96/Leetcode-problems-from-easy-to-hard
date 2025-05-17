class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        # Edge case: if the input is empty, return an empty list
        if not digits:
            return []

        # Mapping from digit to corresponding letters
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Start with an initial list containing an empty string
        result = [""]

        # Loop through each digit in the input
        for digit in digits:
            if digit not in digit_to_letters:
                continue  # skip invalid characters

            # Temporary list to build new combinations
            temp = []

            # For every combination already built so far
            for combination in result:
                # Append each possible letter for current digit
                for letter in digit_to_letters[digit]:
                    temp.append(combination + letter)

            # Update result with new combinations
            result = temp

        return result


        '''
        result = []

        if len(digits) < 1:
            return result
        
        key_value_pairs = {
                            "2" : "abc",
                            "3" : "def",
                            "4" : "ghi",
                            "5" : "jkl",
                            "6" : "mno",
                            "7" : "pqrs",
                            "8" : "tuv",
                            "9" : "wxyz"
                            }        

        def backtracker(index, current_string):
            if index == len(digits):
                result.append(current_string)
                return
            
            letters = key_value_pairs[digits[index]]

            for letter in letters:
                backtracker(index + 1, current_string + letter)

        backtracker(0, "")
        return result'''



def main():
    digits = input("Enter the digits: ")
    obj1 = Solution()
    result = obj1.letterCombinations(digits)
    print(result)

if __name__ == "__main__":
    main()