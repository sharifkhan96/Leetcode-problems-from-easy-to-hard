class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # If negative, convert to 32-bit two's complement equivalent
        if num < 0:
            num += 2 ** 32

        hex_chars = "0123456789abcdef"
        result = ""

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num //= 16

        return result


# time comp: O(log₁₆(n)) ≈ O(log₂(n))
# space comp: o(1)


def main():
    num = 26
    obj1 = Solution()
    print(obj1.toHex(num))


if __name__ == "__main__":
    main()