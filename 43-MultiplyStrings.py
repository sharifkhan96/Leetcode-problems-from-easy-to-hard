class Solution:
    def MultiplyStrings(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # rev both strings to make multiplication easier (start from least significant digit)
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(m):
            for j in range(n):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                result[i + j] += digit1 * digit2  # add product to the correct place
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # rem leading zeros and convert to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))


def main():
    string1 = "23"
    string2 = "22"
    obj1 = Solution()
    print(obj1.MultiplyStrings(string1, string2))  # o/p: 506


if __name__ == "__main__":
    main()
