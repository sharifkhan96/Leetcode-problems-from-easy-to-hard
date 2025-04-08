
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_number = 0
        temporary_number = x

        while temporary_number != 0:
            digit = temporary_number % 10
            reversed_number = reversed_number * 10 + digit
            temporary_number = temporary_number // 10

        return reversed_number == x


def main(): 
    int1 = int(input("Provide a number for Palindrom checking: "))
    #int1 = 121
    solution1 = Solution()
    result = solution1.isPalindrome(int1)
    if result:
        print(f"The {int1} is a palindrome")
    else:
        print(f"The {int1} is not a palidnrome.")

if __name__ == "__main__":
    main()
