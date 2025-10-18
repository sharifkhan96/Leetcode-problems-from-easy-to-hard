class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        # i -> child, j -> cookie
        i = j = 0  

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # cooooooooooooooooooooooooooooooooooookie satisfies this child
                i += 1
            # weee move to next cookie (used or too small)
            j += 1

        return i  # number of happy children


# time comp: O(n log n + m log m)
# space comp: O(1)

def main():
    g = [1, 2]
    s = [1, 2, 3]

    obj = Solution()
    print(obj.findContentChildren(g, s))  # Output: 1


if __name__ == "__main__":
    main()
