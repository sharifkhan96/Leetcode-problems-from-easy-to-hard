class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        # optimezed solution: O(n)
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr
        
        
        # O(n*n), starting from left to right
        # n = len(arr)
        # for i in range(n):
        #     if i == n - 1:
        #         arr[i] = -1
        #     else:
        #         max_right_value = arr[i + 1]
        #         for j in range(i + 2, n):
        #             if arr[j] > max_right_value:
        #                 max_right_value = arr[j]
        #         arr[i] = max_right_value
        # return arr



def main():
    array = [17, 18, 5, 4, 6, 1]
    obj1 = Solution()
    resulting_array = obj1.replaceElements(array)
    print(resulting_array)

if __name__ == "__main__":
    main()