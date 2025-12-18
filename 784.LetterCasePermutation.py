'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
'''

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        
        def backtrack(index, path):
            if index == len(s):
                result.append(path)
                return
            
            if s[index].isalpha():
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())

            else:
                backtrack(index + 1, path + s[index])
            
    
        backtrack(0, "")
        return result

# time comp: 
# space comp: 



class main():
    s = "a1b2"
    obj = Solution()
    print(obj.letterCasePermutation(s))

if __name__ == "__main__":
    main()