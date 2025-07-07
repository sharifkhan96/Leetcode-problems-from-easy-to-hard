class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # works locally but not accepted by leetcode because of space at teh end of the string case
        # for i in s.strip().split()[::-1]:
        #     if not s:
        #         return 0
        #     return len(i)
        #     break

        words = s.strip().split()
        if not s:
            return 0
        return len(words[-1])
        

        # jsut curios to print 
        # for i in range(len(s)):
        #     print(i, s[i])


# complexities:
# time: O(n) because of the striping 
# space: O(n) because of the storage of splitted list

def main():
    string1 = "luffy is still joyboy"
    obj = Solution()
    result = obj.lengthOfLastWord(string1)
    print("Length of the last word in ", string1, " is: ", result)


if __name__ == "__main__":
    main()