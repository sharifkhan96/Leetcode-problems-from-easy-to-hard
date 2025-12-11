class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # convert to list for in-place edits

        for i in range(0, len(s), 2 * k):
            # reverse the first k characters
            s[i : i + k] = reversed(s[i : i + k])

        return "".join(s)





def main():
    input = "abcdefg",
    k = 2
    obj = Solution()
    print(obj.reverseStr(input, k))

if __name__ == "__main__":
    main()
