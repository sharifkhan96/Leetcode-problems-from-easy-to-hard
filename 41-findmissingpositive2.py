import time

class MissingPositiveGame:
    def __init__(self, nums):
        self.nums = nums

    def animate_swap(self, i, j):
        print(f"\n🔄 Swapping nums[{i}]={self.nums[i]} ↔ nums[{j}]={self.nums[j]}")
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        print("Current array:", self.nums)
        time.sleep(0.6)

    def find_missing_positive(self):
        n = len(self.nums)
        i = 0

        print("\n🎯 Starting arrangement of numbers:", self.nums)
        time.sleep(0.8)

        while i < n:
            correct_index = self.nums[i] - 1
            if 1 <= self.nums[i] <= n and self.nums[i] != self.nums[correct_index]:
                self.animate_swap(i, correct_index)
            else:
                i += 1

        print("\n✅ Final arranged array:", self.nums)
        time.sleep(0.8)

        for i in range(n):
            if self.nums[i] != i + 1:
                print(f"\n❌ Found mismatch at index {i}: Expected {i+1}, got {self.nums[i]}")
                print(f"➡️  First missing positive is: {i + 1}")
                return i + 1

        print(f"\n🎉 All positions are correct! Missing = {n + 1}")
        return n + 1


def main():
    print("✨ Welcome to the Missing Positive Finder Game ✨")
    nums = [3, 4, -1, 1]
    print("Input array:", nums)

    game = MissingPositiveGame(nums)
    result = game.find_missing_positive()

    print("\n🏁 Final Answer:", result)
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
