class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        length = len(arr)
        zeros = arr.count(0)

        # We go backwards to avoid overwriting unprocessed elements
        for i in range(length - 1, -1, -1):
            if i + zeros < length:
                arr[i + zeros] = arr[i]

            if arr[i] == 0:
                zeros -= 1
                if i + zeros < length:
                    arr[i + zeros] = 0
     
        
def main():
    array = [1, 0, 2, 0, 3, 4]
    #array = int(input("enter nums having zeros: "))
    obj1 = Solution()
    obj1.duplicateZeros(array)
    print(array)  # Output: [1, 2, 0, 0, 3, 4, 0, 0]

if __name__ == "__main__":
    main()
