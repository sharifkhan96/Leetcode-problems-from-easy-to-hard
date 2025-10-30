from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            # step 1: sooooooooooooooooort each word to get a key
            key = ''.join(sorted(word))
            # step 2: add it to the dictionary
            anagrams[key].append(word)

        # step 3: return the grouped lists
        return list(anagrams.values())
    

# time complexity: O(n * k log k)
# space complexity O(n * k)


# example usage:
def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    obj = Solution()
    print(obj.groupAnagrams(strs))  # output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]

if __name__ == "__main__":
    main()
