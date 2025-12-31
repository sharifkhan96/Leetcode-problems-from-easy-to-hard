# time & space complexity: O(n) and O(1) respectively


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

        

def main():
    obj = Solution()
    values = [3, 2, 3]
    print(obj.majorityElement(values))

if __name__ == "__main__":
    main()
