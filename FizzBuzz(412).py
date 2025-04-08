class Solution:
    """
    Given an integer n, return a string array answer (1-indexed) where:

    - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    - answer[i] == "Fizz" if i is divisible by 3.
    - answer[i] == "Buzz" if i is divisible by 5.
    - answer[i] == i (as a string) if none of the above conditions are true.
    """

    def fizzBuzz(self, n: int) -> list[str]:
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans


def main():
    # Input from the user
    number = int(input("Provide an integer: "))
    obj1 = Solution()
    
    # Call fizzBuzz and store the result
    result = obj1.fizzBuzz(number)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
