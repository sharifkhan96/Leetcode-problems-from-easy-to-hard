from functools import reduce
from operator import xor
from itertools import chain

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        # one step approacah
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                row[i], row[j] = row[j] ^ 1, row[i] ^ 1
                i += 1
                j -= 1
        return image
    
    # time comp: O(n*m) ==> O(n)
    # space comp: O(1)
        
        '''
        # two step approach
        result = []
        for sublist in image:
            reversed_sublist = sublist[::-1]
            inverted_sublist = [1 - x for x in reversed_sublist]
            result.append(inverted_sublist)

        return result
        
# time comp: O(n*m) ==> O(n)
# space comp: O(n)
        '''

class main():
    image = [[1,1,0],[1,0,1],[0,0,0]]
    
    obj1 = Solution()
    print(obj1.flipAndInvertImage(image))




if __name__ == "__main__":
    main()