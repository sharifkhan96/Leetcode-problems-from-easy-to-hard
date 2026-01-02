
# time and space complexity: O(n), and O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        

def main():
    obj1 = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(obj1.maxArea(height))

if __name__ == "__main__":
    main()
