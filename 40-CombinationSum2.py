class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # sort to help skip duplicates
        
        def backtrack(start, current_combination, rem_target):
            if rem_target == 0:
                result.append(list(current_combination))
                return
            if rem_target < 0:
                return
            
            prev = -1  # track previous candidate at this recursion level
            for i in range(start, len(candidates)):
                # skip duplicate numbers at the same recursion depth
                if candidates[i] == prev:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i+1, current_combination, rem_target - candidates[i])
                current_combination.pop()
                
                prev = candidates[i]  # update previous candidate
        
        backtrack(0, [], target)
        return result

#time comnp:O(n^(T/m))
#space comp: O(T/m)

def main():
    candidates = [10,1,2,7,6,1,5] # [2, 3, 6, 7]
    target = 8
    obj = Solution()
    print(obj.combinationSum(candidates, target))


if __name__ == "__main__":
    main()
