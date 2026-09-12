class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            nonlocal count

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # found palindrome
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)      # odd palindrome
            expand(i, i + 1)  # even palindrome

        return count


def main():
    s = input("enter string: ")

    solution = Solution()
    print(solution.countSubstrings(s))


if __name__ == "__main__":
    main()