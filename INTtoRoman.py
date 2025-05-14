class Solution:
    def intToRoman(self, num: int) -> str:
        # Value-symbol pairs, ordered from largest to smallest
        values =  [1000, 900, 500, 400, 100, 90,  50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD","C", "XC","L", "XL","X","IX","V","IV","I"]

        result = ""

        # Loop through each value-symbol pair
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result  

# the time and space complexities are:
# time: O(1) because the loops only runs constant times in this case, 13 times
# space: O(1) we have not used any additional space


def main():
    numb = int(input("enter in integer for roman number: "))
    obj1 = Solution()
    result = obj1.intToRoman(numb)
    print(result)

if __name__ == "__main__":
    main()