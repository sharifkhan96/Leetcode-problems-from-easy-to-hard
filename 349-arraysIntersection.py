class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)   # '&' gives the intersection
        

# time comp: O(n + m)
# space comp: O(n + m)

def main():
    nums1 = [1, 2, 2, 3, 1]
    nums2 = [2, 2, 3, 4]
    obj = Solution()
    print("Intersection:", obj.intersection(nums1, nums2))


if __name__ == "__main__":
    main()
