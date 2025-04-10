class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        if not arr:
            return 0, []
        tracker = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[tracker] = arr[i]
                tracker += 1
                               
        return tracker, arr[:tracker]
        
        
def main():
    nums = [1,1,1,2,3,3,3,4]
    obj1 = Solution()
    k, filtered_array = obj1.removeDuplicates(nums)
    print("Remaining elements in array: ",filtered_array)
    print("Remaining elements in array: ",k)
    #print("length of k: ",len(k))

if __name__ == "__main__":
    main()