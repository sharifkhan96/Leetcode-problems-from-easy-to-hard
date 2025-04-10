class Solution1:
    def deleting_start_array(self, arr: list[int]) -> None:
        print("Before:", arr)

        for i in range(len(arr)-1):
            arr[i] = arr[i+1]

        # removes the duplicate shit
        # arr.pop()
        # del arr[-1]
        arr[:] = arr[:-1]
        print("After:", arr)

    def deleting_anywhere_array(self, arr: list[int], index: int) -> None:
        print("Before:", arr)

        for i in range(index, len(arr) -1):
            arr[i] = arr[i+1]
            
        arr[:] = arr[:-1]

        print("After:", arr)



def main():
    nums1 = [1,2,3,4]
    index = int(input("enter any index for deletion: "))
    obj1 = Solution1()
    # result = obj1.deleting_start_array(nums1)
    result = obj1.deleting_anywhere_array(nums1, index)

if __name__ == "__main__":
    main()
