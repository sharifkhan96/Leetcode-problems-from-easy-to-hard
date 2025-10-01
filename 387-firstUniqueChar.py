class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        frequency = Counter(s)

        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
            
        return -1

# time comp: O(n)
# space comp: O(1)


def main():
    string = input("enter your string: ")
    obj = Solution()
    print("First non-repeated char is at index: ", obj.firstUniqChar(string))


if __name__ == "__main__":
    main()