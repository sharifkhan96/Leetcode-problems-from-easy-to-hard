class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0
        # power = 31

        for _ in range(32):
            # below two commented lines are equivalent to line 12
            # result = (n & 1) << power
            # power -= 1

            result = (result << 1) | n & 1
            n >>= 1

        return result
    
# time and space complexity: O(1), and O(1) since the bit is 2^32-1

def main():
    obj1 = Solution()
    n = 5
    # 00000000000000000000000000000000101
    # 10100000000000000000000000000000000

    print(obj1.reverseBits(n))

if __name__ == "__main__":
    main()
