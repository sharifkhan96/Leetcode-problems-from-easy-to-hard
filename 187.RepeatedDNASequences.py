class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            substring = s[i:i+10]
        
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        
        return list(repeated)


def main():
    
    s = input("Enter DNA sequence: ")
    solution = Solution()
    result = solution.findRepeatedDnaSequences(s)
    print("Repeated DNA sequences:", result)


if __name__ == "__main__":
    main()
