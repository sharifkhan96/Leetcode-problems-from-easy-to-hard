class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


# time comp: O(n)
# space comp: O(n)


class main():
    abc = 3
    
    obj1 = Solution()
    print(obj1.countBits(abc))




if __name__ == "__main__":
    main()