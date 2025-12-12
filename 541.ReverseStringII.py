class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # convert to list for in-place edits

        for i in range(0, len(s), 2 * k):
            # reverse the first k characters
            s[i : i + k] = reversed(s[i : i + k])

        return "".join(s)
        # time comp: O(n)
        # space comp: O(n)

        '''
        # 2 pointer sol:
        class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for i in range(0, len(s), 2 * k):
            left = i
            right = min(i + k - 1, len(s) - 1)

            # reverse using two pointers
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

        '''




def main():
    input = "abcdefg"
    k = 2
    obj = Solution()
    print("Our string: ", input, " before reversing by k chars.")
    print("Our String: ", obj.reverseStr(input, k), " after reversing by k chars.")

if __name__ == "__main__":
    main()
