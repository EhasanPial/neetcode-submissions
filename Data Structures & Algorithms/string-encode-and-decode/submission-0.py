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
            j = i
            if s[j].isdigit():
                l = 0
                while s[j] != "#":
                    l = l * 10 + int(s[j])
                    j += 1
                temp = ""  # new string

                j += 1
                while l > 0:
                    temp += s[j]
                    j += 1
                    l -= 1

                res.append(temp)
                i = j
        return res
