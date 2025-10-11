from collections import Counter

class Solution:
    def findDifference(self, s: str, t: str) -> str:
        '''
        # xor approach
        xor_val = 0
        for ch in s:
            xor_val ^= ord(ch)
        for ch in t:
            xor_val ^= ord(ch)
        
        #for ch in s+t:
        #   xor_val ^= ord(ch)
        

        return chr(xor_val)
        '''

        myCounter = Counter(t) # count the freq of each char in t string

        for ch in s: # loop over s string
            myCounter[ch] -= 1 # decrement the freq of ch located in both s & t
        
            if myCounter[ch] == 0: # if freq of an existed char is zero,
                del myCounter[ch] #  then delete it ultimately


        for ch in myCounter: # here , we locate the char which is added extra to t or s
            return ch
        
        return "" # just being defensive to avoid any crash or empty string provided

# time comp: O(n+m) -> O(n)
# space comp: O(K) -> O(1) for english alphabet



def main():
    stringS = "sharif"
    stringT = "sharifa"

    obj1 = Solution()
    print(obj1.findDifference(stringS, stringT))


if __name__ == "__main__":
    main()