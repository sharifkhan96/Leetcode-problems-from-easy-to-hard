from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # step 1
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        result = ""

        # step two
        for char in order:
            if char in freq:
                result += char * freq[char]
                del freq[char]
                #freq[char].pop()


        # step three
        for char, count in freq.items():
            result += char * count


        return result
        


        
#time comnp:O(n + m), n=counting of s and m=arranging of order
#space comp: o(n) n=fro storing freq map

def main():
    order = "cba"
    s = "abcd"
    obj = Solution()
    print(obj.customSortString(order, s))


if __name__ == "__main__":
    main()