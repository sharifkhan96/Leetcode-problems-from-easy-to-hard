from typing import List

class Codec:
    # time comp: o(n ^2)
    # space comp: O(n)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        
    # time comp: o(n)
    # space comp: O(n)
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result




def main():
    dummy_input = ["Hello","World"]
    print('original input', dummy_input)
    solution = Codec()

    print('encoding...')
    encoded = solution.encode(dummy_input)
    print(encoded)

    print('Decoding...')
    decoded = solution.decode(encoded)
    print(decoded)



if __name__ == "__main__":
    main()