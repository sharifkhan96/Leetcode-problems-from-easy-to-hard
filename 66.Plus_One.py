from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
   
      len_digits = len(digits)

      for i in range(len_digits - 1, -1, -1):
         if digits[i] < 9:
            digits[i] += 1
            return digits
         digits[i] = 0

      return [1] + digits


#complexiities :
# time: O(n) since we iterate on all elements
# space O(1) since we kinda use in-place except if all 9s comes in


def main():
   values = [1,9,8]   #[int(i) for i in input()]
   obj = Solution()
   rsult = obj.plusOne(values)
   print(rsult)



if __name__ == "__main__":
   main()