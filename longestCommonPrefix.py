class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        first = strs[0]

        for i in range(len(first)):
            current_string = first[i]
            for otherStrings in strs[1:]:
                if i >= len(otherStrings) or otherStrings[i] != current_string:
                    return first[:i]
        
        # This return must be outside the for loop
        return first                   


def main():
    string1 = ["flower", "flow", "flight"]
    obj1 = Solution()
    result = obj1.longestCommonPrefix(string1)
    print(result)


if __name__ == "__main__":
    main()
