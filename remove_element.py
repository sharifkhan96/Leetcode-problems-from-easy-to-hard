class Solution:
    def removeElement(self, arr: list[int], val: int) -> int:
        insert_position = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[insert_position] = arr[i]
                insert_position += 1
                               
        return insert_position, arr[:insert_position]
            
        #list comprehension
        # arr[:] = [x for x in arr if x != val]
        # return len(arr)

        #using remove
        # while val in arr:
        #     arr.remove(val)
        # return len(arr)
        
        
def main():
    nums = [3,2,2,3,4,5]
    val = 3
    obj1 = Solution()
    k, filtered_array = obj1.removeElement(nums, val)
    print("Remaining elements in array: ",filtered_array)
    print("Remaining elements in array: ",k)
    #print("length of k: ",len(k))

if __name__ == "__main__":
    main()