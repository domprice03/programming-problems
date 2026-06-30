class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            for idx, char in enumerate(s):
                if char == "#":
                    num = int(s[0:idx])
                    break
            # Start from idx+1 to exclude "#" as well.
            strs.append(s[idx+1:idx+num+1])
            s = s[idx+num+1:]
        return strs
