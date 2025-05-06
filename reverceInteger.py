class Solution:
    def reverse(self, x: int) -> int:
        # 1: split the integer into a list
        # 2: bring the last elements to the first
        # 3: and move the initial elements further down the list
        # 4: make the list unsplit and return
        #[int(i) for i in str(x)]
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        reversed_str = str(x_abs)[::-1]
        reversed_int = int(reversed_str) * sign

        if -2**31 <= reversed_int <= 2**31 - 1:
            return reversed_int
        else:
            return 0
        

        '''
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res
        '''


def main():
    integer1 = int(input("enter your integer to be reversed: ")) # ie 123: 321
    obj1 = Solution()
    result = obj1.reverse(integer1)
    print(result)

if __name__ == "__main__":
    main()