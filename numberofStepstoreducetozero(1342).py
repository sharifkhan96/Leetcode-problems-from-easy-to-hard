class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)
        else:
            return 1 + self.numberOfSteps(num - 1)
    """
    # alternative recursive solution
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)
    """



def main():
    number = 123
    obj1 = Solution()
    result = obj1.numberOfSteps(number)
    print(result)

if __name__ == "__main__":
    main()
        