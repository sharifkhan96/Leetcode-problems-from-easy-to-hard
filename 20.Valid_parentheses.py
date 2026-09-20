import re
class Solution:

    def isValid(self, s: str) -> bool:

        '''
        stack86 = []

        hashmap86 = {")":"(", "}":"{","]":"["}

        for char in s:
            if char in hashmap86:
                if stack86 and stack86[-1] == hashmap86[char]:
                    stack86.pop()
                else:
                    return False
            else:
                stack86.append(char)
        return not stack86
        '''

        '''
        for char in s:
            if char in hashmap1.values():
                stack1.append(char)
            elif char in bracket_map:
                if not stack1 or stack[-1] != hashmap1[char]:
                    return False
                stack1.pop()
            else:
                continue

        return len(stack1) == 0
        '''

# time: o(n)
# space: o(n)

        
        p = re.compile("\[\]|\(\)|\{\}")
        changed = 1
        while (s.__sizeof__() and changed):
            s, changed = p.subn("", s)
            
        if len(s) == 0 : return True
        return False
# o(n^2)

#note: we CAN solve it via a second approach, jsut by tweaking the logic .. 


def main():
    string1 = "()[{}]"
    obj1 = Solution()
    result = obj1.isValid(string1)
    print(result)


if __name__ == "__main__":
    main()