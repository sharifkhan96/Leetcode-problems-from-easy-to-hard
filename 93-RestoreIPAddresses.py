class Solution:
    def restoreIpAddresses(self, s: str):
        result = []

        def backtrack(start, path):
            # this is our base case: 4 segments and end of string reached
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            # we try segments of length 1,2, and 3
            for length in range(1, 4):
                if start + length > len(s):   # out of bounds
                    break

                segment = s[start:start + length]

                # invalid segment checks:
                #  Leading zero ("01", "00")
                #  Value > 255
                if (segment.startswith("0") and length > 1) or int(segment) > 255:
                    continue

                # chooooooooooooooooose segment and recurse for next parts
                backtrack(start + length, path + [segment])

        # start recursion
        backtrack(0, [])

        return result


# time comp: O(3^4) which is 12 char input
# space comp: O(4)

def main():
    s = "25525511135"
    obj = Solution()
    print(obj.restoreIpAddresses(s))  # output: ['255.255.11.135', '255.255.111.35']


if __name__ == "__main__":
    main()
