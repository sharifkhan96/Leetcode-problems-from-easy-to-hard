class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current_combination, rem_target):
            if rem_target == 0:
                result.append(list(current_combination))
                return
            if rem_target < 0:
                return 
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, rem_target - candidates[i])
                current_combination.pop()
                

        backtrack(0, [], target)

        return result

        
#time comnp:O(n^(T/m))
#space comp: O(T/m)

def main():
    candidates = [2,3,6,7]
    target = 7 
    obj = Solution()
    print(obj.combinationSum(candidates, target))


if __name__ == "__main__":
    main()