class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        result = []

        min_diff = arr[1] - arr[0]

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff


        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == min_diff:
                result.append([arr[i], arr[i+1]])

        return result


# time comp: O(n log n)
# space comp: O(n)


class main():
    abc = [4, 2, 1, 3]
    
    obj1 = Solution()
    print(obj1.minimumAbsDifference(abc))




if __name__ == "__main__":
    main()