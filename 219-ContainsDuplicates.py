class Solution:
    def containsDuplicates2(self, list1: list, k: int)-> bool:
        seen = set()
        
        for listi in range(len(list1)):
            
            current_listi = list1[listi]

            if current_listi in seen:
                return True
            seen.add(current_listi)

            if len(seen) > k:
                seen.remove(list1[listi - k])
        
        return False


        
#time comnp:O(n)
#space comp: o(k)

def main():
    list1 = [1, 2, 3, 1, 2, 3]
    k = 2

    obj = Solution()
    print(obj.containsDuplicates2(list1, k))


if __name__ == "__main__":
    main()