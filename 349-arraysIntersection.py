class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)   # '&' gives the intersection
        

# time comp: O(n + m)
# space comp: O(n + m)

'''
class Solution:
    def intersection(self, nums1, nums2):
        # Step 1: Convert nums1 into a set (unique values)
        set1 = set(nums1)

        # Step 2: Create an empty set to store the intersection
        result = set()

        # Step 3: Loop through nums2 and check which numbers also appear in set1
        for num in nums2:
            if num in set1:
                result.add(num)

        # Step 4: Convert to list before returning (as LeetCode expects a list)
        return list(result)
'''

def main():
    nums1 = [1, 2, 2, 3, 1]
    nums2 = [2, 2, 3, 4]
    obj = Solution()
    print("Intersection:", obj.intersection(nums1, nums2))


if __name__ == "__main__":
    main()
