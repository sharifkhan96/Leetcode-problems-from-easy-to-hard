class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        # backtracking fun
        def backtrack(open, close, current_string):
            # we chaeck if we crossed all the combinations, if so, return if not skip and move to sec2
            if len(current_string) == 2 * n:
                result.append(current_string)
                return 
            
            # sec2: if not all "(" are used, we put "(". if used, skip and move to sec3 
            if open < n:
                backtrack(open + 1, close, current_string + "(")

            # sec3: if not ")" are used, we put ")". if used, skip
            if close < open:
                backtrack(open, close + 1, current_string + ")")


        
        

        
        backtrack(0, 0, "")

        return result





def main():
    numberOfParenthesis = int(input("enter n for pairs of parenthesis: "))
    obj1 = Solution()
    result = obj1.generateParenthesis(numberOfParenthesis)
    print(result)



if __name__ == "__main__":
    main()