class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        
        
        length1 = len(arr)
        if length1 < 3:
            return False
        
        i = 0

        # checking the climb up of mountain fucking arrayyyyy
        while i + 1 < length1 and arr[i] < arr[i + 1]:
            i += 1

        # now check the peak to avoid being it the first or last elemento :)
        if i == 0 or i == length1 - 1:
            return False
        
        # checcking the climb down of mountain everest, sorry mountain decreasing array
        while i + 1 < length1 and arr[i] > arr[i + 1]:
            i += 1

        return i == length1 -1 



def main():
    array1 = [0,3,2,1]
    obj1 = Solution()
    result = obj1.validMountainArray(array1)
    print(result)

if __name__ == "__main__":
    main()