from functools import reduce
from operator import xor
from itertools import chain

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        #rev = image[::-1]
        for sublist in image:
            sublist.reverse()
        #print(image)

        res = 0 
        for num in image:
            # XOR the current number with the result
            res ^= num  

        return res

# time comp: O(n)
# space comp: O(n)


class main():
    image = [[1,1,0],[1,0,1],[0,0,0]]
    
    obj1 = Solution()
    print(obj1.flipAndInvertImage(image))




if __name__ == "__main__":
    main()