from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sorting
        # anagrams = defaultdict(list)

        # for word in strs:
        #     # step 1: sooooooooooooooooort each word to get a key
        #     key = ''.join(sorted(word))
        #     # step 2: add it to the dictionary
        #     anagrams[key].append(word)

        # # step 3: return the grouped lists
        # return list(anagrams.values())
    
        # # time complexity: O(n * k log k)
        # # space complexity O(n * k)


        # using 26-character frequency count
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())
        # time comp: O(N*M)
        # space comp: O(n * 26) => o(N)


# example usage:
def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Random List: ", strs)
    obj = Solution()
    print("Anagramed List: ", obj.groupAnagrams(strs))  # output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]

if __name__ == "__main__":
    main()
