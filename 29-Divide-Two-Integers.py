
# class SolutionSubtract: O(dividend/divisor)
#     def division1(self, dividend, divisor):
#         if dividend == 0:
#             return "undefined" # or we can handle the error via error funcs
#         quotient = 0
#         is_negative = (dividend < 0) != (divisor < 0)

#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         while dividend >= divisor:
#             dividend -= divisor
#             quotient += 1


#         if is_negative:
#             quotient = -quotient
#         return quotient

class SolutionBitWise: #O(log n)
    def division1(self, dividend, divisor):
        if dividend == 0:
            return 0
        if divisor == 0:
            return "undefined"  # Prevent divide-by-zero

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Prevent overflow for 32-bit signed int

        # Determine the sign of the result
        is_negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers only
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Repeat until dividend is smaller than divisor
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double temp and multiple as long as it doesn't exceed dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the largest multiple of divisor we found
            dividend -= temp
            quotient += multiple

        # Apply sign
        if is_negative:
            quotient = -quotient

        return quotient





def main():
    dividend = 12
    divisor = 3

    obj1 = SolutionBitWise()
    result = obj1.division1(dividend, divisor)
    print(result)

    # obj1 = SolutionSubtract()
    # result = obj1.division1(dividend, divisor)
    # print(result)



if __name__ == "__main__":
    main()