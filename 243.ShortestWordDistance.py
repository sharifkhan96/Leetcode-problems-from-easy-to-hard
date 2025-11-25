class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
    
        # optimal solutionnnnnnnnnnnnnn
        shortestDistance = len(wordsDict)
        pos1 = -1
        pos2 = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            elif wordsDict[i] == word2:
                pos2 = i
            
            if pos1 != -1 and pos2 != -1:
                shortestDistance = min(shortestDistance, abs(pos1-pos2))

        return shortestDistance

        # time comp: O(n)
        # space comp: O(1)
               
        
        '''
        # bruteforcce solution

        shortestDis = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        shortestDis = min(shortestDis, abs(i-j))
        return shortestDis
        # time comp: O(n^2)
        # space comp: O(1)        
        '''
        
        

class main():
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"

    obj1 = Solution()
    print(obj1.shortestDistance(wordsDict, word1, word2))


if __name__ == "__main__":
    main()