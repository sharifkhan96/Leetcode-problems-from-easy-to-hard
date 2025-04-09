class Solution:
    def merge(self, nums1 : list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        print(nums2)  

        # easy-peazzzy but unoptimized solution     
        # nums1[m:] = nums2
        # nums1.sort()
        # O(n log n) becomes:
        # O((m + n) log(m + n))


        # time complexity: O(m+n)
        # O(1) 
        i = m -1 
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


        print(nums1)
        print(nums2)
        
        
def main():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    
    obj1 = Solution()
    result = obj1.merge(nums1, 3, nums2, 3)
    

if __name__ == "__main__":
    main()
        