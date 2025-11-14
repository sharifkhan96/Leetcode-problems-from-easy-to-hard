class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # here, we should check the mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
                
            else:
                s_to_t[char_s] = char_t


            # here, we do the reverse chaeck of mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


        
#time comnp:O(n)
#space comp: o(1)

def main():
    s = "egg"
    t = "add"
    obj = Solution()
    print(obj.isIsomorphic(s, t))


if __name__ == "__main__":
    main()