class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # keep looping until single digit
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10  # get last digit
                num //= 10             # remove last digit
            num = sum_digits
        return num




def main():
    num = 40
    solution = Solution()
    result = solution.addDigits(num)
    print(result)


if __name__ == "__main__":
    main()