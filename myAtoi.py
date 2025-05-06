class Solution:
    def myAtoi(self, s: str) -> int:
       s = s.lstrip()
       if not s:
           return 0
       
       sign = 1
       i = 0
       if s[0] in ['-', '+']:
           sign = -1 if s[0] == '-' else 1
           i += 1

        
       num = 0
       while i < len(s) and s[i].isdigit():
           num = num * 10 + int(s[i])
           i += 1

       num *= sign
       integer_min, integer_max = -2**31, 2**31 - 1
       if num < integer_min:
           return integer_min
       elif num > integer_max:
           return integer_max
       return num
    #
    #time complexity is O(n) since we are scanning each char in worse case at least once
    #space complexity is o(1) since wer not using any extra data structuressssssss
       



def main():
    input1 = input("enter the value: ")
    obj1 = Solution()
    resutl = obj1.myAtoi(input1)
    print(resutl)


if __name__ == "__main__":
    main()