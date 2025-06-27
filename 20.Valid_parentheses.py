class Solution:
    def isValid(self, s: str) -> bool:
        
        stack1 = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        

        for char in s:
            if char in bracket_map.values():
                stack1.append(char)
            elif char in bracket_map:
                if not stack1 != bracket_map[char]:
                    return False
                stack1.pop()
            else:
                continue

        return len(stack1) == 0


# time: o(n)
# space: o(n)

#note: we CAN solve it via a second approach, jsut by tweaking the logic .. 


def main():
    string1 = "()[{}]"
    obj1 = Solution()
    result = obj1.isValid(string1)
    print(result)


if __name__ == "__main__":
    main()