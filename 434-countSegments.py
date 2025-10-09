class Solution:
    def countSegments(self, s: str)-> int:
        count = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1

        return count
        


        
#time comnp:O(n)
#space comp: o(1)

def main():
    str1 = " hello there heheheh"
    obj = Solution()
    print(obj.countSegments(str1))


if __name__ == "__main__":
    main()