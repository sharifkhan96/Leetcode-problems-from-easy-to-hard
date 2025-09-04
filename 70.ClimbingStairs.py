class Solution:
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


def main():
    # Example inputs
    n = int(input("Enter the number of steps: "))
    
    solution = Solution()
    result = solution.climbStairs(n)
    
    print(f"Number of distinct ways to climb {n} steps = {result}")


if __name__ == "__main__":
    main()
