class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

#time comnp:O(n log n + m log m)
#space comp: o(1)

def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    obj = Solution()
    print(obj.intersect(nums1, nums2))


if __name__ == "__main__":
    main()