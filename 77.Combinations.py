'''
 - we are given n and k integers to make k combinations til n
 -  order does not matter since its a combnation problem meaning to say that [1, 2] and [2, 1] are treated as one combo :)
'''

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result
    
    # time comp: O(K. n!/(n-k)!k!) ==> O(k.(n/k))
    # space comp: O(K. n!/(n-k)!k!) ==> O(k.(n/k))

class main():
    n = 4
    k = 2
    obj1 = Solution()
    print(obj1.combine(n, k))


if __name__ == "__main__":
    main()