
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:      
                sum += int(b[j])
                j -= 1

            result += (str(sum % 2))

            carry = sum // 2

        return "".join(reversed(result))



            


# time comp: o(max(len(a), len(b))
# spac3 comp: o(max(len(a), len(b))

def main():
    a = "011"
    b = "100"
    # a = 101
    # b = 100
    obj = Solution()
    result = obj.addBinary(a, b)
    print(result)

if __name__ == "__main__":
    main()