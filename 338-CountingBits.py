class Solution:
    def countBits(self, n: int) -> list[int]:

        # o(n log n) solution
        # return [i.bit_count() for i in range(n + 1)]

        '''
        result = []
        for i in range(n + 1):
            count = 0

            x = i
            while x > 0:
                count += x & 1
                x >>= 1
            result.append(count)

        return result
        '''


        # dp solution
        # time comp: O(n)
        # space comp: O(n)
        '''
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
        '''

        # Kernighan Algo: O(number of 1 bits in given input number)
        
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                x = x & (x - 1)
                count += 1
        return count
        

class main():
    abc = 7
    
    obj1 = Solution()
    print(obj1.countBits(abc))




if __name__ == "__main__":
    main()