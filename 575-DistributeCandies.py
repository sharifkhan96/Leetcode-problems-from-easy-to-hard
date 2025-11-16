class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_type = len(set(candyType))
        max_eatable = len(candyType) // 2

        return min(unique_type, max_eatable)



# time comp: O(n) for inserting elements in set
# space comp: O(n) for storing  //          //


class main():
    candyType = [1,1,2,3]
    
    obj1 = Solution()
    print(obj1.distributeCandies(candyType))




if __name__ == "__main__":
    main()