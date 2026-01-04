class Solution:

    def isValid(self, s: str) -> bool:
        
        stack1 = []
        hashmap1 = {')': '(', ']': '[', '}': '{'}
        
        for element in s:
            if stack1 and (element in hashmap1 and stack1[-1] == hashmap1[element]):
                stack1.pop()
            else:
                stack1.append(element)

        return not stack1

        # for char in s:
        #     if char in hashmap1.values():
        #         stack1.append(char)
        #     elif char in bracket_map:
        #         if not stack1 != hashmap1[char]:
        #             return False
        #         stack1.pop()
        #     else:
        #         continue

        # return len(stack1) == 0


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