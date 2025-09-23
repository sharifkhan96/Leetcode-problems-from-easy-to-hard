class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid      # store the floor candidate
                left = mid + 1
            else:
                right = mid - 1

        return ans


def main():
    sol = Solution()
    print("Input: 4 => Output:", sol.mySqrt(4))   # 2
    print("Input: 8 => Output:", sol.mySqrt(8))   # 2 (since sqrt(8) ~ 2.82)
    print("Input: 1 => Output:", sol.mySqrt(1))   # 1
    print("Input: 0 => Output:", sol.mySqrt(0))   # 0


if __name__ == "__main__":
    main()
