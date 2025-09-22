class Solution:
    # stack based solution
    '''def longestValidParentheses(self, s: str) -> int:
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

        return maxLength'''
    
    # two pointer solution
    # time comp: O(n)
    # space comp: O(1)
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        maxLength = 0

        # Pass 1: Left to Right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right > left:
                left = right = 0  # reset (invalid substring)

        # Pass 2: Right to Left (to catch unmatched '(' cases)
        left = right = 0
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1

            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left = right = 0  # reset (invalid substring)

        return maxLength


def main():
    s1 = "(()"
    s2 = ")()())"
    solution = Solution()
    print("Input:", s1, "=> Longest valid parentheses length:", solution.longestValidParentheses(s1))
    print("Input:", s2, "=> Longest valid parentheses length:", solution.longestValidParentheses(s2))


if __name__ == "__main__":
    main()
