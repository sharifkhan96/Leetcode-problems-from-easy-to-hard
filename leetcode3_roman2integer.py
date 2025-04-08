class Solution:
    def romanToInt(self, s: str) -> int:
        print("The string is : ", s)

        translated_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0
        prev_number = 0

        #s = s.replace("IV", "IIII").replace("IX", "VIIII")
        #s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        #s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for character in reversed(s):

            current_number= translated_nums[character]

            if current_number < prev_number:
                number -= current_number
            else:
                number += current_number

            prev_number = current_number


        return number



def main():

    string1 = input("Enter a valid roman letter: ").upper()

    obj1 = Solution()

    result = obj1.romanToInt(string1)
    print(f"The {string1} is equal to {result}")

if __name__ == "__main__":
    main()
        