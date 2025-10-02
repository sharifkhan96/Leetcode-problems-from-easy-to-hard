class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)

        return False
    

# time comp: O(n)
# space comp: O(n)


def main():
    array1 = [1, 3, 2, 1, 9]
    obj = Solution()

    print(obj.containsDuplicate(array1))



if __name__ == "__main__":
    main()