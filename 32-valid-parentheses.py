class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index to handle edge cases
        maxLength = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # push index of '('
            else:
                stack.pop()  # try to match with '('
                if not stack:
                    stack.append(i)  # reset base if no match
                else:
                    # valid substring length = currentIndex - last unmatched index
                    maxLength = max(maxLength, i - stack[-1])

        return maxLength


def main():
    s1 = "(()"
    s2 = ")()())"
    solution = Solution()
    print("Input:", s1, "=> Longest valid parentheses length:", solution.longestValidParentheses(s1))
    print("Input:", s2, "=> Longest valid parentheses length:", solution.longestValidParentheses(s2))


if __name__ == "__main__":
    main()
