class Solution:
    # dp solution : O(n) & O(n)
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    '''
    recursive but not optimal solution:
    def climbStairs(self, n: int) -> int:
        # Base case: if there's only 1 step, only 1 way
        if n == 1:
            return 1
        if n == 2:
            return 2
        return climbStairs(n - 1) + climbStairs(n - 2)
    '''
    
    '''
    def climbStairs(self, n: int) -> int:
        # Base case: if there's only 1 step, only 1 way
        if n == 1:
            return 1
        
        # Base cases: f(1) = 1, f(2) = 2
        first, second = 1, 2
        
        # Loop from step 3 up to n
        for i in range(3, n + 1):
            # Update like Fibonacci sequence
            first, second = second, first + second
        
        return second
    '''


    '''
    # space optimized solution: # O(n), O(1)
    if n <= 2:
        return n

    
    prev2 = 1
    prev1 = 2

    for _ in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
    '''


def main():
    # Example inputs
    n = int(input("Enter the number of steps: "))
    
    solution = Solution()
    result = solution.climbStairs(n)
    
    print(f"Number of distinct ways to climb {n} steps = {result}")


if __name__ == "__main__":
    main()
