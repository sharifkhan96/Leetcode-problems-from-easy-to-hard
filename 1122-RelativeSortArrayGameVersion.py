import time
from collections import Counter

class RelativeSortGame:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def play(self):
        print("🎯 Welcome to the Relative Sort Game 🎯")
        print("Arr1:", self.arr1)
        print("Arr2 (Order Guide):", self.arr2)
        time.sleep(1)

        freq = Counter(self.arr1)
        result = []

        print("\n🔍 Step 1: Counting occurrences...")
        time.sleep(0.5)
        print("Frequency Map:", dict(freq))
        time.sleep(1)

        print("\n🔄 Step 2: Sorting according to Arr2 order...")
        for num in self.arr2:
            if num in freq:
                print(f"➡️ Adding {num} x {freq[num]} to result")
                result.extend([num] * freq[num])
                del freq[num]
                print("Current result:", result)
                time.sleep(0.7)

        print("\n✨ Step 3: Adding remaining numbers (sorted ascending)...")
        leftover = sorted(freq.keys())
        for num in leftover:
            print(f"➡️ Adding {num} x {freq[num]} to result")
            result.extend([num] * freq[num])
            print("Current result:", result)
            time.sleep(0.7)

        print("\n🏁 Final Sorted Result:", result)
        return result


def main():
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    game = RelativeSortGame(arr1, arr2)
    game.play()


if __name__ == "__main__":
    main()
