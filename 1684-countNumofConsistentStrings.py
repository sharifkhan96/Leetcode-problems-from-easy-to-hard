class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        
        # allowed = set(allowed)
        # return sum(all(c in allowed for c in word) for word in words)

        allowed_set = set(allowed)
        count = 0

        for word in words:
            is_consistent = True
            for ch in word:
                if ch not in allowed_set:
                    is_consistent = False
                    break

            if is_consistent:
                count += 1

        return count

# time comp: O(n * m)
# space comp: O(1)



class main():

    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    obj = Solution()
    print(obj.countConsistentStrings(allowed, words))

if __name__ == "__main__":
    main()