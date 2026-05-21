class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = 0 # length pointer
            while s[i+j] != '#':
                j += 1
            l = int(s[i:i+j])
            i += j
            i += 1 # move to the word after '#'
            ss = s[i:i+l]
            res.append(ss)
            i += l

        return res
