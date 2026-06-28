class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for word in strs:
            encoded_strs += (str(len(word)) + '#' + word)
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            decoded_strs.append(word)
            i = j + 1 + length
        return decoded_strs
