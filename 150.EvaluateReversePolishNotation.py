class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack1 = []

        for t in tokens:
            if t not in "+-*/":
                stack1.append(int(t))
            else:
                r, l = stack1.pop(), stack1.pop()

                if t == "+":
                    stack1.append(l + r)
                elif t == "-":
                    stack1.append(l + r)
                elif t == "*":
                    stack1.append(l * r)
                else:
                    stack1.append(int(float(l) / r))

        return stack1.pop()           

# time & space complexity: O(n) and O(n)




def main():
    tokens = ["2","1","+","3","*"]
    #tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    obj1 = Solution()
    print(obj1.evalRPN(tokens))



if __name__ == '__main__':
    main()
    