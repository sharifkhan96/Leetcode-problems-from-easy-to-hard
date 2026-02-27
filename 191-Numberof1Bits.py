
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # bit minipulation, more efficient as it avoids processing 0s
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
        # mod solution
        # result = 0
        
        # while n > 0:
        #     result += n % 2
        #     n = n >> 1

        # return result
    
'''
# time and space complexity: O(1), and O(1) since the bit is 2^32-1

we are given with a decimal [bit set(binary number)], we need to return the number of ones in the given number
ie : 10 decimal to binary is : 101, so we return 2 since we have 2 ones in the binary nuumber of 10
if given 11 which when converted to binary is 3 and have 2 ones
'''
        

def main():
    obj1 = Solution()
    n = 3
    print(obj1.hammingWeight(n))

if __name__ == "__main__":
    main()
