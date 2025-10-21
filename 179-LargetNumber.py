from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # step 1: we convert all integers to strings
        nums = list(map(str, nums))
        
        # step 2: define custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1    # b should come before a
            else:
                return 0

        # step 3: sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # step 4: join the sorted numbers
        result = ''.join(nums)
        
        # step 5: handle edge case like ["0","0"]
        return '0' if result[0] == '0' else result


        
#time comp;: O(n log n · k)        sorting: o(n log n), joinging the string: o(n.k)
#space comp: o(n.k)

def main():
    nums = [10, 2]
    obj = Solution()
    print(obj.largestNumber(nums))


if __name__ == "__main__":
    main()